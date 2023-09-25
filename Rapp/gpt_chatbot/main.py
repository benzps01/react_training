import openai

openai.api_key = "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"


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        print("")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = None
        while response is None:
            print("Loading your answer...")
            print("")
            response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
        print("")
