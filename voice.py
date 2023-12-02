import random

def greet():
    responses = ["Hello!", "Hi there!", "Greetings!", "Hey!", "name"]
    return random.choice(responses)

def respond(message):
    message = message.lower()

    if "how are you" in message:
        return "I'm just a computer program, but I'm doing well. Thanks for asking!"

    elif "your name" in message:
        return "I'm a chatbot, and you can call me ChatGPT."

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        return "I'm not sure how to respond to that. Ask me something else."

def main():
    print("Chatbot: " + greet())

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
