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
    
    "Test Options": {
        "Test": "Test answer",
    }
}

def quiz(stack_name):
    stack = flashcard_stacks[stack_name]
    questions = list(stack.keys())
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)
    missed_questions = []

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
            print("Incorrect.")

    print(f"You got {score} out of {total_questions} correct.")

    if missed_questions:
        print("Let's try those missed questions again:")
        while missed_questions:
            question = random.choice(missed_questions)
            missed_questions.remove(question)
            meaning = stack[question]
            print(question)
            user_answer = input("Your answer: ")

            if user_answer.lower() == 'exit':
                print("Exiting the quiz...")
                return

            match_ratio = fuzz.ratio(user_answer.lower(), meaning.lower())
            if match_ratio >= 80:
                print("Correct! (Close enough)")
            elif user_answer.lower() == meaning.lower():
                print("Correct!")
            else:
                print("Incorrect. The answer is:", meaning)

# Display available stacks
print("Available stacks:")
for stack in flashcard_stacks.keys():
    print(f"- {stack}")

# Loop until a valid stack name is entered
stack_name = ""
while stack_name not in flashcard_stacks:
    stack_name = input("\nEnter the stack name: ")
    if stack_name not in flashcard_stacks:
        print("Invalid stack name. Please choose from the list.")

# Start the quiz
quiz(stack_name)