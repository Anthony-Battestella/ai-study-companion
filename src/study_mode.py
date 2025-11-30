import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(question, level):
    prompt = f"""
    You are an AI study tutor. The student is level: {level}.
    Answer the following question clearly and with an example:

    Question: {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content


def study_session(user):
    print("\n🧠 Study Mode Activated. Type 'exit' to return.\n")

    while True:
        question = input("Ask a question: ")

        if question.lower() == "exit":
            break

        answer = generate_answer(question, user['level'])
        print("\nAI 🤖:\n" + answer + "\n")
