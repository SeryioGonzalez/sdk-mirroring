# Copyright (c) Microsoft. All rights reserved.

import asyncio

from azure.identity import AzureCliCredential

from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

# Simulate a conversation with the agent
USER_INPUT = "In which contenent is Korea?"

async def main():
    # 1. Create the agent by specifying the service
    print("Creating the agent...")
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(credential=AzureCliCredential()),
        name="demo-agent",
        instructions="Answer questions about the world in one sentence.",
    )

    print("Starting conversation with the agent...")

    print(f"# User: {USER_INPUT}")
    # 2. Invoke the agent for a response
    response = await agent.get_response(
        messages=USER_INPUT ,
    )
    # 3. Print the response
    print(f"# {response.name}: {response}")


if __name__ == "__main__":
    asyncio.run(main())