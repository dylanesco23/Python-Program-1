from openai import OpenAI

client = OpenAI()

print("AI Chatbot (type 'quit' to exit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Bot: Goodbye!")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )

    print("Bot:", response.choices[0].message.content)
