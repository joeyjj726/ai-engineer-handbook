import requests
import json

url = "http://localhost:11434/api/chat"

payload = {
    "model": "qwen3:8b",
    "messages": [
        {
        "role": "user",
        "content": "我叫 Joey"
    },
    {
        "role": "assistant",
        "content": "很高興認識你，Joey！"
    },
    {
        "role": "user",
        "content": "我叫什麼名字？"
    }
    ],
    "stream": False
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print()

result = response.json()
print("模型：", result["model"])
print()
print("回答：")
print(result["message"]["content"])