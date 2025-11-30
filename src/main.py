from study_mode import study_session
from quiz_module import quiz_session
from flashcards import flashcard_menu
from user_profile import load_user, save_user
from rich.console import Console
from rich.table import Table

console = Console()

def display_menu():
    table = Table(title="AI Study Companion Menu")

    table.add_column("#", justify="center", style="cyan", no_wrap=True)
    table.add_column("Option", style="white")

    table.add_row("1", "Study Mode (Ask Questions)")
    table.add_row("2", "Quiz Mode")
    table.add_row("3", "View Progress")
    table.add_row("4", "Flashcards")
    table.add_row("5", "Save & Exit")

    console.print(table)

def main():
    console.print("\n📚 [bold green]Welcome to the AI Study Companion![/bold green]\n")
    name = console.input("[bold yellow]Enter your name:[/bold yellow] ")

    user = load_user(name)

    while True:
        display_menu()
        choice = console.input("\n[bold cyan]Choose an option:[/bold cyan] ")

        if choice == "1":
            study_session(user)
        elif choice == "2":
            quiz_session(user)
        elif choice == "3":
            console.print(f"\n📈 [bold green]Current Level:[/bold green] {user['level']}")
            console.print(f"⭐ [bold blue]Quizzes Completed:[/bold blue] {user['quizzes']}")
        elif choice == "4":
            flashcard_menu()
        elif choice == "5":
            save_user(user)
            console.print("\n💾 [bold magenta]Progress saved. Goodbye![/bold magenta]\n")
            break
        else:
            console.print("[red]❌ Invalid choice. Try again.[/red]")

if __name__ == "__main__":
    main()
