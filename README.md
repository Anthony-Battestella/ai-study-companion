# 📚 AI Study Companion

An interactive, terminal-based study tool powered by AI.
It helps users learn more effectively through explanations, quizzes, flashcards, and customizable learning styles.

💡 Designed as a personal learning assistant that adapts to different study preferences.

| Feature                   | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| 🧠 Study Mode             | Ask any question and receive an explanation                         |
| 🎨 Learning Styles        | "Explain Like I'm 5", summary mode, detailed mode, or example-based |
| 🎯 Interactive Quizzes    | AI-generated questions with automatic grading                       |
| 🗂 Flashcards             | Create, review, and delete flashcards                               |
| 📈 User Progress Tracking | Tracks quiz history and retains user state                          |
| 🔐 Offline-Friendly       | Built-in fallback responses if OpenAI credits/connection fail       |


| Component   | Implementation                      |
| ----------- | ----------------------------------- |
| Language    | Python                              |
| AI Model    | OpenAI GPT (fallback mode included) |
| UI Styling  | Rich Terminal Formatting            |
| Persistence | JSON-based local storage            |
