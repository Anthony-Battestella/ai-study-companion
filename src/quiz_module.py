import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_quiz(topic):
    prompt = f"Create a short 3-question quiz on: {topic}. Include an answer key."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content


def quiz_session(user):
    print("\n📘 Quiz Mode Activated. Type 'exit' to return.\n")
    
    topic = input("What topic should the quiz be about? ")

    if topic.lower() == "exit":
        return

    quiz = generate_quiz(topic)
    
    print("\n📖 Quiz:\n")
    print(quiz)

    user['quizzes'] += 1
