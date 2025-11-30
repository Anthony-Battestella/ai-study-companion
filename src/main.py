from study_mode import study_session
from quiz_module import quiz_session
from user_profile import load_user, save_user

def main():
    print("\n📚 Welcome to the AI Study Companion!\n")
    name = input("Enter your name: ")

    user = load_user(name)

    while True:
        print("\n------ MENU ------")
        print("1. Study Mode (Ask Questions)")
        print("2. Quiz Mode")
        print("3. View Progress")
        print("4. Save & Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            study_session(user)
        elif choice == "2":
            quiz_session(user)
        elif choice == "3":
            print(f"\n📈 Current Level: {user['level']}")
            print(f"⭐ Quizzes Completed: {user['quizzes']}")
        elif choice == "4":
            save_user(user)
            print("\n💾 Progress saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

