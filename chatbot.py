print("AI Chatbot (type 'exit' to stop)\n")

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you today?")

    # Basic conversation
    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking")

    elif "your name" in user or "name" in user:
        print("Bot: I am an AI chatbot created using Python.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day.")
        break

    elif user == "exit":
        print("Bot: Chat ended.")
        break

    # College / Student related
    elif "college" in user:
        print("Bot: College life is exciting! What are you studying?")

    elif "course" in user or "bca" in user:
        print("Bot: BCA with AI is a great choice.")

    elif "exam" in user:
        print("Bot: Stay calm and revise well. You’ll do great!")

    elif "marks" in user:
        print("Bot: Marks are important, but learning matters more.")

    # AI & Tech
    elif "ai" in user:
        print("Bot: Artificial Intelligence is transforming the world.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a core part of AI where systems learn from data.")

    elif "python" in user:
        print("Bot: Python is widely used in AI, ML, and data science.")

    elif "programming" in user:
        print("Bot: Programming helps solve real-world problems using logic.")

    # Fun responses
    elif "time" in user:
        from datetime import datetime
        now = datetime.now()
        print("Bot: Current time is", now.strftime("%H:%M:%S"))

    elif "date" in user:
        from datetime import datetime
        today = datetime.now()
        print("Bot: Today's date is", today.strftime("%d-%m-%Y"))

    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs.")

    elif "thanks" in user:
        print("Bot: You're welcome!")

    # Default response
    else:
        print("Bot: Sorry, I didn't understand that. Try asking something else!")