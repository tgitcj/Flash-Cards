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
        "A high-level programming language": "Python",
        "A general-purpose programming language": "Java",
        # ... more languages
    },
    
    "Test Options": {
        "Test": "Test answer",
    }
}

def quiz(selected_stacks):
    # Combine selected stacks into one
    combined_stack = {}
    for stack_name in selected_stacks:
        combined_stack.update(flashcard_stacks[stack_name])
    
    questions = list(combined_stack.keys())
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)
    missed_questions = []

    for question in questions:
        meaning = combined_stack[question]
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
            meaning = combined_stack[question]
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
print("- Random (selects a random stack)")

# Loop until valid stacks are selected or the user exits
while True:
    stack_input = input("\nEnter one or more stack names: ").strip()

    if stack_input.lower() == 'exit':
        print("Exiting the program...")
        break

    # Split the input into multiple stacks
    stack_names = [name.strip() for name in stack_input.split(",")]
    
    # Handle "Random" as one of the options
    if "Random" in stack_names:
        # Remove "Random" and filter out already selected stacks
        stack_names.remove("Random")
        available_stacks = [name for name in flashcard_stacks if name not in stack_names]
        
        if not available_stacks:
            print("No stacks available for random selection. All stacks are already chosen.")
            continue
        
        random_stack = random.choice(available_stacks)
        print(f"Adding random stack: {random_stack}")
        stack_names.append(random_stack)

    # Validate stack names
    invalid_stacks = [name for name in stack_names if name not in flashcard_stacks]

    if invalid_stacks:
        print(f"Invalid stack names: {', '.join(invalid_stacks)}. Please choose valid stacks.")
    else:
        print(f"Starting quiz with: {', '.join(stack_names)}")
        quiz(stack_names)
        break
