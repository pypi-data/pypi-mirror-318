import requests
import json


def send_chat_request(content):
    # API endpoint
    url = "http://localhost:8000/v1/chat/completions"

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    # Payload
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": content}
        ],
        "stream": True
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, json=data, stream=True)

        # Check if response is successful
        if response.status_code == 200:
            for chunk in response.iter_lines():
                if chunk:
                    parsed_chunk = json.loads(chunk.decode("utf-8").replace("data: ", ""))
                    # if parsed_chunk['finish_reason']!='stop':
                    if parsed_chunk.get('finish_reason')!='stop':
                        print(parsed_chunk['choices'][0]['delta']['content'],end="",flush=True)
        else:
            print(f"Error: Received status code {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    send_chat_request("Hello")
