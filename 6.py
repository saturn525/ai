print("Customer Support Chatbot")
print("Type 'bye' to exit")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "price":
        print("Bot: Please visit our website for pricing details.")

    elif user == "product":
        print("Bot: We have laptops, mobiles and accessories.")

    elif user == "timing":
        print("Bot: Our shop is open from 9 AM to 9 PM.")

    elif user == "bye":
        print("Bot: Thank you! Visit again.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
