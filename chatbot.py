import openai

# Set your OpenAI API key
openai.api_key = "your_api_key_here"


def chatbot():
    print("AI Chatbot: Hello! Type 'exit' to stop chatting.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AI Chatbot: Goodbye!")
            break

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )

        reply = response["choices"][0]["message"]["content"]
        print(f"AI Chatbot: {reply}")


# Run the chatbot
chatbot()
