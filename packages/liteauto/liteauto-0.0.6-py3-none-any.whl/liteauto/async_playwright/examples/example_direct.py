import asyncio
from liteauto.async_playwright._oai import ChatHFClient


async def main():
    hf_client = await ChatHFClient.create(headless=True)
    try:
        # For non-streaming response
        if False:  # Toggle this to switch between streaming and non-streaming
            res = await hf_client.completions.create([
                {
                    "role": "system",
                    "content": "your name is santhosh"
                },
                {
                    "role": "user",
                    "content": 'what is your name?'
                }
            ])
            print(res)

        # For streaming response
        else:
            stream = await hf_client.completions.create([
                {
                    "role": "system",
                    "content": ""
                },
                {
                    "role": "user",
                    "content": 'what is your name?'
                }
            ], stream=True)

            async for chunk in stream:
                # Print just the content from the chunk
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end='', flush=True)

    finally:
        # Make sure to close the client
        await hf_client.close()


if __name__ == '__main__':
    asyncio.run(main())