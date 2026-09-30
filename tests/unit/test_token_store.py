from __future__ import annotations

import json
import os
import stat
import sys
from pathlib import Path

import httpx
import pytest

from shellrent_sdk.auth import FileTokenStore, MemoryTokenStore, OAuth2Auth
from tests.support import (
    API_URL,
    CLIENT_SECRET,
    FakeApi,
    FakeClock,
    credentials,
    health_response,
    token_response,
)

posix_only = pytest.mark.skipif(sys.platform == "win32", reason="POSIX permissions")


def mode(path: Path) -> int:
    return stat.S_IMODE(path.stat().st_mode)


# MemoryTokenStore


def test_memory_store_keeps_values_until_they_expire() -> None:
    clock = FakeClock()
    store = MemoryTokenStore(clock=clock)

    store.set("key", "value", 10)
    assert store.get("key") == "value"
    clock.now += 10
    assert store.get("key") is None


def test_memory_store_deletes_values() -> None:
    store = MemoryTokenStore()
    store.set("key", "value", 10)
    store.delete("key")
    store.delete("missing")

    assert store.get("key") is None


# FileTokenStore


def test_file_store_keeps_values_between_instances(tmp_path: Path) -> None:
    FileTokenStore(tmp_path).set("key", "value", 10)

    assert FileTokenStore(tmp_path).get("key") == "value"
    assert FileTokenStore(tmp_path).get("missing") is None


def test_file_store_ignores_expired_values(tmp_path: Path) -> None:
    clock = FakeClock()
    store = FileTokenStore(tmp_path, clock=clock)

    store.set("key", "value", 10)
    clock.now += 9
    assert store.get("key") == "value"
    clock.now += 1
    assert store.get("key") is None


def test_file_store_deletes_values(tmp_path: Path) -> None:
    store = FileTokenStore(tmp_path)
    store.set("key", "value", 10)
    store.delete("key")
    store.delete("missing")

    assert store.get("key") is None
    assert list(tmp_path.iterdir()) == []


def test_file_store_set_with_expired_ttl_deletes(tmp_path: Path) -> None:
    store = FileTokenStore(tmp_path)
    store.set("key", "value", 10)
    store.set("key", "value", 0)

    assert store.get("key") is None


def test_file_store_ignores_damaged_files(tmp_path: Path) -> None:
    store = FileTokenStore(tmp_path)
    (tmp_path / "key.json").write_text("{not json")
    (tmp_path / "other.json").write_text(json.dumps({"value": 1, "expires_at": "tomorrow"}))

    assert store.get("key") is None
    assert store.get("other") is None


@pytest.mark.parametrize("key", ["../key", "a/b", ".hidden", ""])
def test_file_store_rejects_keys_that_are_not_file_names(tmp_path: Path, key: str) -> None:
    with pytest.raises(ValueError, match="Invalid key"):
        FileTokenStore(tmp_path).set(key, "value", 10)


@posix_only
def test_file_store_creates_private_directory_and_files(tmp_path: Path) -> None:
    directory = tmp_path / "cache" / "shellrent-sdk"
    old_umask = os.umask(0o022)
    try:
        FileTokenStore(directory).set("key", "value", 10)
    finally:
        os.umask(old_umask)

    assert mode(directory) == 0o700
    assert mode(directory / "key.json") == 0o600


def test_file_store_writes_through_a_temporary_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    replaced: list[tuple[str, str]] = []
    real_replace = os.replace

    def replace(src: str, dst: str) -> None:
        replaced.append((str(src), str(dst)))
        real_replace(src, dst)

    monkeypatch.setattr(os, "replace", replace)
    FileTokenStore(tmp_path).set("key", "value", 10)

    [(src, dst)] = replaced
    assert Path(src).parent == tmp_path
    assert dst == str(tmp_path / "key.json")
    assert [p.name for p in tmp_path.iterdir()] == ["key.json"]


def test_file_store_keeps_the_old_file_when_the_write_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    store = FileTokenStore(tmp_path)
    store.set("key", "old", 10)

    def replace(src: str, dst: str) -> None:
        raise OSError("disk full")

    monkeypatch.setattr(os, "replace", replace)
    with pytest.raises(OSError, match="disk full"):
        store.set("key", "new", 10)

    assert store.get("key") == "old"
    assert [p.name for p in tmp_path.iterdir()] == ["key.json"]


def test_file_store_default_directory(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / "xdg"))
    assert FileTokenStore().directory == tmp_path / "xdg" / "shellrent-sdk"

    monkeypatch.setenv("XDG_CACHE_HOME", "relative/path")
    monkeypatch.setenv("HOME", str(tmp_path / "home"))
    monkeypatch.setenv("USERPROFILE", str(tmp_path / "home"))
    assert FileTokenStore().directory == tmp_path / "home" / ".cache" / "shellrent-sdk"


# With OAuth2Auth


def test_a_new_process_reuses_the_token_in_the_file(tmp_path: Path) -> None:
    api = FakeApi(token_response("token-1"), health_response(), health_response())

    for _ in range(2):
        auth = OAuth2Auth(credentials(), FileTokenStore(tmp_path))
        with httpx.Client(base_url=API_URL, auth=auth, transport=api.transport()) as client:
            client.get("/api/health")

    assert len(api.token_requests) == 1
    [file] = tmp_path.iterdir()
    assert "token-1" in file.read_text()
    assert CLIENT_SECRET not in file.read_text()
    assert CLIENT_SECRET not in file.name


def test_an_expired_token_in_the_file_is_not_used(tmp_path: Path) -> None:
    clock = FakeClock()
    api = FakeApi(
        token_response("token-1"), health_response(), token_response("token-2"), health_response()
    )

    auth = OAuth2Auth(credentials(), FileTokenStore(tmp_path, clock=clock), clock=clock)
    with httpx.Client(base_url=API_URL, auth=auth, transport=api.transport()) as client:
        client.get("/api/health")

    clock.now += 540
    auth = OAuth2Auth(credentials(), FileTokenStore(tmp_path, clock=clock), clock=clock)
    with httpx.Client(base_url=API_URL, auth=auth, transport=api.transport()) as client:
        client.get("/api/health")

    assert len(api.token_requests) == 2
    assert api.api_requests[-1].headers["Authorization"] == "Bearer token-2"
