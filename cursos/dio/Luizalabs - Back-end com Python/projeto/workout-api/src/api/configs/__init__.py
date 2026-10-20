"""Pacote de configuração da aplicação.

`app` é resolvido sob demanda (PEP 562) para que importar submódulos como
`api.configs.database` ou `api.configs.dependencies` não monte a aplicação
nem gere import circular com `api.controllers`.
"""

from typing import Any

__all__ = ["app"]


def __getattr__(name: str) -> Any:
    if name == "app":
        from api.configs.main import app

        return app
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
