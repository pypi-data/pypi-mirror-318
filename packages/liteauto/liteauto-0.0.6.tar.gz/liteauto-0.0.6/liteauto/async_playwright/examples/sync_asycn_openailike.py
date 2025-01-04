import asyncio
from liteauto.async_playwright.openai_client_classes import OpenAI,AsyncOpenAI,OpenAIError


# Sync usage example
def sync_example():
    client = OpenAI(base_url="http://localhost:8000")

    # Non-streaming
    response = client.chat.completions(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    )
    print(f"Non-streaming response: {response.choices[0]['message']['content']}")

    # Streaming
    stream = client.chat.completions(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ],
        stream=True
    )
    print("Streaming response: ", end="", flush=True)
    for chunk in stream:
        if chunk['choices'][0]['delta'].get('content'):
            print(chunk['choices'][0]['delta']['content'], end="", flush=True)
    print()



async def async_example():
    client = AsyncOpenAI(base_url="http://localhost:8000")
    try:
        # Non-streaming
        try:
            response = await client.chat.completions(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Hello!"}
                ]
            )
            print(f"Response: {response.choices[0]['message']['content']}")
        except OpenAIError as e:
            print(f"Error occurred: {e.message}")
            if e.status_code:
                print(f"Status code: {e.status_code}")
            if e.response:
                print(f"Full response: {e.response}")

        # Streaming example
        try:
            stream = await client.chat.completions(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Hello!"}
                ],
                stream=True
            )
            print("Streaming response: ", end="", flush=True)
            async for chunk in stream:
                if chunk['choices'][0]['delta'].get('content'):
                    print(chunk['choices'][0]['delta']['content'], end="", flush=True)
            print()
        except OpenAIError as e:
            print(f"Streaming error occurred: {e.message}")
    finally:
        await client.close()


if __name__ == "__main__":
    # Run sync example
    # print("Running sync example:")
    # sync_example()

    # Run async example
    print("\nRunning async example:")
    asyncio.run(async_example())