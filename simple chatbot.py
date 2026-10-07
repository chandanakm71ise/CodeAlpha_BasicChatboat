def chatbot():
    print("Hello! I am your chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "hello":
            print("Bot: Hi! Nice to meet you.")
        elif user_input.lower() == "how are you":
            print("Bot: I'm fine, thanks.")
        elif user_input.lower() == "thanks":
            print("Bot: You are welcome!")
        elif user_input.lower() == "bye":
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: I'm sorry, I don't understand that.")

chatbot()