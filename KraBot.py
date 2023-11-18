import random

def kra_bot():
    responses = [
        "Kra",
        "Kra Kra",
        "Kra Kra Kra",
        "Kra Kra Kra Kra",
        "Kra Kra Kra Kra Kra"
    ]

    while True:
        user_input = input("Ask me anything: ")
        if user_input.lower() == "bye":
            print("Goodbye!")
            break
        print(random.choice(responses))

# Run the bot
kra_bot()
