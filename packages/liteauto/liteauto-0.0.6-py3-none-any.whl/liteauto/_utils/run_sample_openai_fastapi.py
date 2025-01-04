import requests
import json
import websocket  # Use websocket-client package instead of websockets

# Base configuration
BASE_URL = "http://localhost:8000"
API_KEY = "your-test-api-key"  # Replace with your API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def chat_completion():
    """Test the chat completions endpoint"""
    url = f"{BASE_URL}/v1/chat/completions"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Hello, how are you?"}
        ]
    }

    response = requests.post(url, json=payload, headers=HEADERS)
    print("\nChat Completion Response:", json.dumps(response.json(), indent=2))


def get_streaming_response(messages, model="gpt-3.5-turbo"):
    """Generator function for streaming chat responses"""
    # Create a WebSocket connection
    ws = websocket.create_connection(
        f"ws://localhost:8000/v1/chat/completions/stream",
        header=["Authorization: Bearer " + API_KEY]
    )

    try:
        # Send the initial message
        payload = {
            "model": model,
            "messages": messages,
            "stream": True
        }
        ws.send(json.dumps(payload))

        # Receive and yield responses
        while True:
            try:
                response = ws.recv()
                if response == '{"finish_reason":"stop"}':
                    break

                chunk = json.loads(response)
                if 'choices' in chunk and chunk['choices']:
                    if 'delta' in chunk['choices'][0] and 'content' in chunk['choices'][0]['delta']:
                        yield chunk['choices'][0]['delta']['content']
            except websocket.WebSocketConnectionClosed:
                break
    finally:
        ws.close()


def streaming_chat():
    """Test the streaming chat completion endpoint"""
    messages = [
        {"role": "user", "content": "Tell me a short story"}
    ]

    for chunk in get_streaming_response(messages):
        print(chunk,end = "",flush=True)


def image_generation():
    """Test the image generation endpoint"""
    url = f"{BASE_URL}/v1/images/generations"
    payload = {
        "prompt": "A beautiful sunset over mountains",
        "n": 2,
        "size": "1024x1024"
    }

    response = requests.post(url, json=payload, headers=HEADERS)
    print("\nImage Generation Response:", json.dumps(response.json(), indent=2))


def embeddings():
    """Test the embeddings endpoint"""
    url = f"{BASE_URL}/v1/embeddings"
    payload = {
        "input": "Hello world",
        "model": "text-embedding-ada-002"
    }

    response = requests.post(url, json=payload, headers=HEADERS)
    print("\nEmbeddings Response:", json.dumps(response.json(), indent=2))


def moderations():
    """Test the moderations endpoint"""
    url = f"{BASE_URL}/v1/moderations"
    payload = {
        "input": "Some text to moderate",
        "model": "text-moderation-latest"
    }

    response = requests.post(url, json=payload, headers=HEADERS)
    print("\nModerations Response:", json.dumps(response.json(), indent=2))


def main():
    # Test all endpoints
    # chat_completion()
    streaming_chat()
    # image_generation()
    # embeddings()
    # moderations()


if __name__ == "__main__":
    main()