import os
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console

# Load environment variables
load_dotenv()

# Initialize console
console = Console()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(question, level, style):
    prompt = f"""
You are an AI study tutor. The student skill level is: {level}.
Apply this learning style: {style}.
Answer the question clearly, with accurate information, and remain friendly.

Question: {question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


def study_session(user):
    console.print("\n🧠 [bold underline]Study Mode Activated[/bold underline]. Type 'exit' to return.\n")

    # 🎨 Learning style selection
    styles = {
        "1": "Explain it like I'm 5: use very simple words",
        "2": "Give a short summary: keep it brief",
        "3": "Explain in detail: include deeper concepts",
        "4": "Give an explanation with multiple real-world examples"
    }

    console.print("\n🎨 [bold]Choose learning style:[/bold]\n")
    for k, v in styles.items():
        console.print(f"{k}. {v}")

    style_choice = console.input("\n[cyan]Select style:[/cyan] ")
    selected_style = styles.get(style_choice, styles["3"])

    # Start Q&A loop
    while True:
        question = console.input("\n[yellow]Ask a question:[/yellow] ")

        if question.lower().strip() == "exit":
            console.print("\n[green]📦 Returning to main menu...[/green]\n")
            break

        console.print("\n🤖 Generating response...\n", style="dim")

        answer = generate_answer(question, user['level'], selected_style)

        console.print("\n📘 [bold cyan]Answer:[/bold cyan]\n")
        console.print(answer + "\n")
