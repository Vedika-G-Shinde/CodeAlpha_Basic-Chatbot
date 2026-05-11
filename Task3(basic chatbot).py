def chatbot():

    responses = {
        "hello": "Hello! Welcome!",
        "hi": "Hi there!",
        "how are you": "I am doing great, thanks!",
        "what is your name": "I am a simple Python chatbot.",
        "bye": "Goodbye! Have a nice day!"
    }

    print("Chatbot Started!")
    print("Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ").lower()

        if user_input in responses:
            print("Bot:", responses[user_input])

        else:
            print("Bot: Sorry, I don't understand that.")


        if user_input == "bye":
            break

chatbot()