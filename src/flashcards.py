import json
from rich.console import Console

console = Console()
FLASHCARD_FILE = "flashcards.json"

def load_flashcards():
    try:
        with open(FLASHCARD_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_flashcards(cards):
    with open(FLASHCARD_FILE, "w") as f:
        json.dump(cards, f, indent=4)

def create_flashcard():
    console.print("\n📝 [bold]Create a Flashcard[/bold]")
    question = console.input("Question: ")
    answer = console.input("Answer: ")

    cards = load_flashcards()
    cards.append({"q": question, "a": answer})
    save_flashcards(cards)

    console.print("[green]✔ Flashcard saved![/green]\n")

def review_flashcards():
    cards = load_flashcards()
    
    if not cards:
        console.print("[red]⚠ No flashcards created yet.[/red]\n")
        return

    console.print("\n📚 [bold]Flashcard Review[/bold]\n")

    for card in cards:
        console.print(f"\n❓ {card['q']}")
        input("Press Enter to reveal answer...")
        console.print(f"👉 {card['a']}\n")

def clear_flashcards():
    """Deletes ALL flashcards after confirmation."""
    console.print("\n⚠️ [bold red]WARNING:[/bold red] This will delete ALL flashcards permanently.")
    confirm = console.input("Type 'DELETE' to confirm: ")

    if confirm == "DELETE":
        save_flashcards([])  # overwrite with empty list
        console.print("[green]✔ All flashcards cleared.[/green]\n")
    else:
        console.print("[yellow]Action cancelled.[/yellow]\n")

def flashcard_menu():
    while True:
        console.print("\n------ FLASHCARDS ------")
        console.print("1. Create Flashcard")
        console.print("2. Review Flashcards")
        console.print("3. Clear All Flashcards")
        console.print("4. Back")

        choice = console.input("\nChoose: ")

        if choice == "1":
            create_flashcard()
        elif choice == "2":
            review_flashcards()
        elif choice == "3":
            clear_flashcards()
        elif choice == "4":
            break
        else:
            console.print("[red]❌ Invalid choice.[/red]")
