# ==========================================
#            PYTHON AI CHATBOT
# ==========================================

import random
from datetime import datetime


def chatbot_response(message):
    message = message.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey"]:
        responses = [
            "Hello! 👋",
            "Hi! How can I help you?",
            "Hey! Nice to meet you."
        ]
        return random.choice(responses)

    # How are you
    elif "how are you" in message:
        return "I'm doing great! Thanks for asking. 😊"

    # Name
    elif "your name" in message:
        return "My name is PythonBot."

    # Time
    elif "time" in message:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # Date
    elif "date" in message:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}."

    # Python
    elif "python" in message:
        return "Python is a popular programming language used for web development, automation, data science and AI."

    # Help
    elif "help" in message:
        return "I can talk about Python, tell you the date and time, and respond to basic greetings."

    # Goodbye
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"

    # Unknown question
    else:
        return "Sorry, I don't understand that yet. Try asking something else."


print("================================")
print("        🤖 PYTHON CHATBOT")
print("================================")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")

    response = chatbot_response(user_message)

    print("Bot:", response)

    if user_message.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break