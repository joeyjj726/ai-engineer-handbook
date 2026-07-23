import requests

URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:8b"

messages: list[dict[str, str]] = []

print("=== Mini ChatGPT ===")
print("輸入 exit 離開")
print()

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    if not user_input:
        continue

    messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
    }

    try:
        response = requests.post(URL, json=payload, timeout=300)
        response.raise_for_status()
        result = response.json()
    except requests.RequestException as error:
        print(f"\nRequest failed: {error}\n")

        # Request 失敗時移除尚未完成的 user message，
        # 避免聊天紀錄留下不完整的一輪。
        messages.pop()
        continue

    answer = result["message"]["content"]

    messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    prompt_tokens = result.get("prompt_eval_count", 0)
    output_tokens = result.get("eval_count", 0)
    eval_duration = result.get("eval_duration", 0)

    print(f"\nAI: {answer}\n")
    print(f"Messages stored: {len(messages)}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Output tokens: {output_tokens}")

    if eval_duration > 0:
        tokens_per_second = output_tokens / (
            eval_duration / 1_000_000_000
        )
        print(f"Generation speed: {tokens_per_second:.2f} tokens/sec")

    print()