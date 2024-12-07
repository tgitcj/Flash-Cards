import random
from fuzzywuzzy import fuzz

# Create a dictionary of flashcards, organized by stack
flashcard_stacks = {
    "IT Acronyms": {        
        "CPU": "Central Processing Unit",
        "RAM": "Random Access Memory",
        "HDD": "Hard Disk Drive",
        "SSD": "Solid State Drive",
        "OS": "Operating System",
        "VPN": "Virtual Private Network",
        "IoT": "Internet of Things",
        "AI": "Artificial Intelligence",
        "ML": "Machine Learning",
        "DL": "Deep Learning"
    },

    "Programming Languages": {
        "Python": "A high-level programming language",
        "Java": "A general-purpose programming language",
        # ... more languages
    },
    # ... more stacks
}

import random
from fuzzywuzzy import fuzz

# ... (rest of the code remains the same)

def quiz(stack_name, missed_questions=None):
    if missed_questions is None:
        missed_questions = []
    stack = flashcard_stacks[stack_name]
    questions = list(stack.keys())
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    for question in questions:
        meaning = stack[question]
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == 'exit':
            print("Exiting the quiz...")
            return

        match_ratio = fuzz.ratio(user_answer.lower(), meaning.lower())
        if match_ratio >= 80:
            print("Correct! (Close enough)")
            score += 1
        elif user_answer.lower() == meaning.lower():
            print("Correct!")
            score += 1
        else:
            missed_questions.append(question)
            print("Incorrect. The answer is:", meaning)

    print(f"You got {score} out of {total_questions} correct.")

    if missed_questions:
        print("Let's try those missed questions again:")
        quiz(stack_name, missed_questions)


# Get user input for the desired stack
stack_name = input("Enter the stack name (e.g., IT Acronyms, Programming Languages): ")

# Start the quiz
quiz(stack_name)
