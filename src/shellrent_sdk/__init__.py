"""Official Python SDK for the Shellrent public API.

The functions of the operations are generated in ``shellrent_sdk.client.api``, one module per tag and
one module per operationId; the models in ``shellrent_sdk.client.models``.
"""

from ._errors import ApiErrorLike, ApiException, unwrap
from ._factory import create_client
from .auth import ClientCredentials, FileTokenStore, MemoryTokenStore, TokenError, TokenStore
from .client.errors import UnexpectedStatus

__all__ = [
    "ApiErrorLike",
    "ApiException",
    "ClientCredentials",
    "FileTokenStore",
    "MemoryTokenStore",
    "TokenError",
    "TokenStore",
    "UnexpectedStatus",
    "create_client",
    "unwrap",
]
