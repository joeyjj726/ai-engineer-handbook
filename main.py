from ollama import chat


def main() -> None:
    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": "你是一個有幫助的 AI 助手，請使用繁體中文回答。",
            },
            {
                "role": "user",
                "content": "請用簡單的方式解釋什麼是大型語言模型。",
            },
        ],
    )

    print(response.message.content)


if __name__ == "__main__":
    main()