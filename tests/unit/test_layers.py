"""auth, http and cli are used by other SDKs, with generated clients of their own."""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

import shellrent_sdk

PACKAGE_DIR = Path(shellrent_sdk.__file__).parent


def imported_modules(path: Path) -> set[str]:
    modules: set[str] = set()
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if node.level:  # Relative to shellrent_sdk, where the modules are.
                module = f"shellrent_sdk.{module}" if module else "shellrent_sdk"
            modules.add(module)
            modules.update(f"{module}.{alias.name}" for alias in node.names)
    return modules


@pytest.mark.parametrize("module", ["auth.py", "http.py", "cli.py"])
def test_does_not_import_the_generated_client(module: str) -> None:
    imports = imported_modules(PACKAGE_DIR / module)

    assert not [name for name in imports if name.startswith("shellrent_sdk.client")]
