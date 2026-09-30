"""Local servers for the tests of proxies and certificates: an HTTP proxy and an HTTPS server."""

from __future__ import annotations

import contextlib
import json
import select
import socket
import ssl
import threading
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

TLS_DIR = Path(__file__).parent / "fixtures" / "tls"
#: Test CA that signed the certificate of the HTTPS server, for 127.0.0.1 and localhost.
CA_FILE = TLS_DIR / "ca.pem"
#: Name of CA_FILE in a directory for SSL_CERT_DIR: the OpenSSL hash of its subject.
CA_HASH_NAME = "2024fd72.0"


class Server(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, handler: type[BaseHTTPRequestHandler]) -> None:
        super().__init__(("127.0.0.1", 0), handler)
        #: Request lines received, such as "GET http://api.test/api/health".
        self.requests: list[str] = []

    @property
    def port(self) -> int:
        return int(self.server_address[1])

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.port}"


class ProxyHandler(BaseHTTPRequestHandler):
    """Answers the requests forwarded to it, and tunnels CONNECT to the host requested."""

    server: Server

    def do_GET(self) -> None:
        self.server.requests.append(f"{self.command} {self.path}")
        if self.path.endswith("/oauth/token"):
            self._reply({"access_token": "token-1", "expires_in": 600})
        else:
            self._reply({"error": 0, "message": "", "data": {"target": self.path}, "meta": None})

    def do_POST(self) -> None:
        self.rfile.read(int(self.headers.get("Content-Length", 0)))
        self.do_GET()

    def do_CONNECT(self) -> None:
        self.server.requests.append(f"CONNECT {self.path}")
        host, port = self.path.rsplit(":", 1)
        with socket.create_connection((host, int(port))) as upstream:
            self.send_response(200, "Connection established")
            self.end_headers()
            sockets = [self.connection, upstream]
            while True:
                readable, _, _ = select.select(sockets, [], [], 5)
                if not readable:
                    break
                for sock in readable:
                    data = sock.recv(65536)
                    if not data:
                        self.close_connection = True
                        return
                    (upstream if sock is self.connection else self.connection).sendall(data)
        self.close_connection = True

    def _reply(self, body: object) -> None:
        content = json.dumps(body).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format: str, *args: object) -> None:
        pass


class HelloHandler(BaseHTTPRequestHandler):
    server: Server

    def do_GET(self) -> None:
        self.server.requests.append(f"GET {self.path}")
        self.send_response(200)
        self.send_header("Content-Length", "5")
        self.end_headers()
        self.wfile.write(b"hello")

    def log_message(self, format: str, *args: object) -> None:
        pass


@contextlib.contextmanager
def serve(server: Server) -> Iterator[Server]:
    thread = threading.Thread(target=server.serve_forever, args=(0.05,), daemon=True)
    thread.start()
    try:
        yield server
    finally:
        server.shutdown()
        server.server_close()


@contextlib.contextmanager
def proxy_server() -> Iterator[Server]:
    with serve(Server(ProxyHandler)) as server:
        yield server


@contextlib.contextmanager
def tls_server() -> Iterator[Server]:
    """HTTPS server with a certificate signed by the test CA: https://localhost:<port>/."""
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(TLS_DIR / "server.pem", TLS_DIR / "server-key.pem")
    server = Server(HelloHandler)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    with serve(server):
        yield server
