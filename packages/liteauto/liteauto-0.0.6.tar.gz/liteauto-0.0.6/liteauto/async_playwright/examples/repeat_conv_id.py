import json
import uuid
from concurrent.futures.thread import ThreadPoolExecutor
from pathlib import Path

import requests

def run_sample(conv_id=None, stream=False):
    url = "http://0.0.0.0:8000/v1/chat/completions"
    payload = {
        "model": "string",
        "messages": [
            {
                "role": "system",
                "content": "Your name is santhosh, tell joke after your name"
            },
            {
                "role": "user",
                "content": "what is your name?"
            }
        ],
        "stream": stream,
        "temperature": 1,
        "max_tokens": 0,
        "conv_id": conv_id
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        if stream:
            for chunk in response.iter_lines(decode_unicode=True):
                # print(chunk)
                yield chunk
                # if chunk:
                #     chunk_data = json.loads(chunk.decode("utf-8")[6:])
                #     print(chunk_data,flush=True)
            final_res  = ""
        else:
            final_res = response.json()
    else:
        final_res = f"Failed to get response: {response.reason}"
    return final_res

if __name__ == "__main__":
    data = {}
    id = str(uuid.uuid4())
    for r in run_sample(id,True):
        print(r,end="",flush=True)


