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
        "A high-level programming language": "Python" ,
        "A general-purpose programming language": "Java",
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

        # First check for an exact match
        if user_answer.strip().lower() == meaning.lower():
            print("Correct!")
            score += 1
        # Then check for a close enough match using fuzzy ratio
        elif fuzz.ratio(user_answer.lower(), meaning.lower()) >= 80:
            print("Correct! (Close enough)")
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

            # Repeat the same checks as above
            if user_answer.strip().lower() == meaning.lower():
                print("Correct!")
            elif fuzz.ratio(user_answer.lower(), meaning.lower()) >= 80:
                print("Correct! (Close enough)")
            else:
                print("Incorrect. The answer is:", meaning)

# Display available stacks
print("Available stacks:")
for stack in flashcard_stacks.keys():
    print(f"- {stack}")
print("- Random (select a random stack)")

# Loop until a valid stack name is entered or the user exits
stack_name = ""
while True:
    stack_name = input("\nEnter the stack name: ")
    if stack_name.lower() == 'exit':
        print("Exiting the program...")
        break
    elif stack_name.lower() == 'random':
        stack_name = random.choice(list(flashcard_stacks.keys()))
        print(f"Randomly selected stack: {stack_name}")
        quiz(stack_name)
        break  # Exit the loop and start the quiz
    elif stack_name in flashcard_stacks:
        quiz(stack_name)
        break  # Exit the loop and start the quiz
    else:
        print("Invalid stack name. Please choose from the list.")