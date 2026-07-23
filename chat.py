import requests

url = "http://localhost:11434/api/chat"

messages = []

print("=== Mini ChatGPT ===")
print("輸入 exit 離開")
print()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # 把使用者訊息加入聊天紀錄
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    payload = {
        "model": "qwen3:8b",
        "messages": messages,
        "stream": False
    }

    response = requests.post(url, json=payload)

    result = response.json()

    answer = result["message"]["content"]

    print(f"\nAI: {answer}\n")

    # 把 AI 回答也加入聊天紀錄
    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )