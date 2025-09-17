# Default behavior: re-export SK agents.
# If you later add custom Agent types or wrappers, define them here and
# they will be preferred over the alias created in __init__.py.
from semantic_kernel.agents import ChatCompletionAgent  # re-export

__all__ = ["ChatCompletionAgent"]
