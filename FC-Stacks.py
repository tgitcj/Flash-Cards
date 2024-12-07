import random

# Create a dictionary of flashcards, organized by stack
flashcard_stacks = {
    "IT Acronyms": {
        "CPU": "Central Processing Unit",
        "RAM": "Random Access Memory",
        # ... more acronyms
    },
    "Programming Languages": {
        "Python": "A high-level programming language",
        "Java": "A general-purpose programming language",
        # ... more languages
    },
    # ... more stacks
}

def quiz(stack_name):
    stack = flashcard_stacks[stack_name]
    score = 0
    total_questions = len(stack)

    for acronym, meaning in stack.items():
        print(acronym)
        user_answer = input("Your answer: ")

        if user_answer.lower() == meaning.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The answer is:", meaning)

    print(f"You got {score} out of {total_questions} correct.")

# Get user input for the desired stack
stack_name = input("Enter the stack name (e.g., IT Acronyms, Programming Languages): ")

# Start the quiz
quiz(stack_name)