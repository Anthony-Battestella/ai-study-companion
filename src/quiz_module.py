import os
import re
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

load_dotenv()
console = Console()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_quiz(topic):
    prompt = f"""
Create a 3-question quiz on: {topic}.
Format it EXACTLY like this:

Q1: question here
A1: correct answer here

Q2: question here
A2: correct answer here

Q3: question here
A3: correct answer here
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content

def parse_quiz(quiz_text):
    questions = re.findall(r"Q\d+: (.+)", quiz_text)
    answers = re.findall(r"A\d+: (.+)", quiz_text)
    return questions, answers

def quiz_session(user):
    console.print("\n📘 [bold underline]Quiz Mode Activated[/bold underline]. Type 'exit' to return.\n")

    topic = console.input("[cyan]What topic should the quiz be about?[/cyan] ")

    if topic.lower() == "exit":
        return
    
    console.print("\n🤖 Generating quiz...\n", style="dim")
    quiz_text = generate_quiz(topic)
    
    questions, answers = parse_quiz(quiz_text)
    
    score = 0

    for i, question in enumerate(questions):
        console.print(f"\n❓ [yellow]{question}[/yellow]")
        user_answer = console.input("Your answer: ")

        correct_answer = answers[i]

        if user_answer.lower().strip() in correct_answer.lower():
            console.print("[green]✔ Correct![/green]")
            score += 1
        else:
            console.print(f"[red]✘ Incorrect.[/red] Correct Answer: [bold]{correct_answer}[/bold]")

    user['quizzes'] += 1
    console.print(f"\n🏁 [bold]Quiz Complete![/bold] Score: {score}/{len(questions)}")

    if score == len(questions):
        console.print("🎉 PERFECT SCORE!")
    elif score > 1:
        console.print("👍 Good work — keep practicing!")
    else:
        console.print("📚 Try again — you’ll get better!")
