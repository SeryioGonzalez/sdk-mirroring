from __future__ import annotations
import importlib

# Semantic Kernel is an implementation dependency
_sk = importlib.import_module("semantic_kernel")
__version__ = getattr(_sk, "__version__", "0+agentic-core-shim")

# Only alias the SK submodules you need.
from ._shim import alias_modules

alias_modules({
    # Facade package for agents (re-exported in agentic_core/agents/__init__.py)
    "agentic_core.agents": "semantic_kernel.agents",
    # Specific connector file path (we'll also provide a local wrapper for extension)
    "agentic_core.connectors.ai.open_ai": "semantic_kernel.connectors.ai.open_ai",
})

# Optional: expose a compatibility check gate you can call from your app
def check_compat(min_version: str | None = None, max_version: str | None = None) -> None:
    from packaging.version import Version
    skv = Version(getattr(_sk, "__version__", "0"))
    if min_version and skv < Version(min_version):
        raise RuntimeError(f"semantic_kernel {skv} < required {min_version}")
    if max_version and skv > Version(max_version):
        raise RuntimeError(f"semantic_kernel {skv} > supported {max_version}")
