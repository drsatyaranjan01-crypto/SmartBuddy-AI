from ai import ask_ai


def main():
    print("=" * 45)
    print("🤖 SmartBuddy AI")
    print("=" * 45)
    print("Type 'exit' to stop.")
    print()

    while True:

        user_message = input("You: ")

        # Exit command
        if user_message.lower().strip() == "exit":
            print("\n👋 SmartBuddy: Bye Satya! See you soon! 😊")
            break

        # Ignore empty messages
        if not user_message.strip():
            continue

        response = ask_ai(user_message)

        print("\n🤖 SmartBuddy:", response)
        print()


if __name__ == "__main__":
    main()