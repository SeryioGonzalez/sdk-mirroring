# Start by re-exporting the SK connector
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion as _SKAzureChatCompletion

class AzureChatCompletion(_SKAzureChatCompletion):
    """
    Drop-in subclass that lets you add Agentic Core–specific defaults or hooks
    without breaking SK compatibility.
    """
    # Example: attach a simple hook or default param
    def __init__(self, *args, **kwargs):
        # You can inject defaults (e.g., telemetry or retries) here
        text= "I am a cloned SDK connector class! "
        print(f"\033[31m{text}\033[0m")
        super().__init__(*args, **kwargs)


__all__ = ["AzureChatCompletion"]
