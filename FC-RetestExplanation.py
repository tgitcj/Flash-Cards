import random
from fuzzywuzzy import fuzz

# Create a dictionary of topics, each containing stacks of flashcards
flashcard_topics = {
    "IT Basics": {
        "IT Acronyms": {        
            "CPU": ("Central Processing Unit", "The CPU processes instructions from programs and manages data."),
            "RAM": ("Random Access Memory", "Temporary storage used by a computer to hold data and programs in use."),
            "HDD": ("Hard Disk Drive", "A traditional storage device with spinning disks to store data."),
            "SSD": ("Solid State Drive", "A faster storage device using flash memory."),
            "IP": ("Internet Protocol", "A set of rules for addressing and routing data across networks."),
        },
        "Hardware Components": {
            "Power Supply Unit": ("PSU", "Converts electrical power into usable power for internal components."),
            "Motherboard": ("Mainboard", "The main circuit board that connects all components."),
            "GPU": ("Graphics Processing Unit", "Handles rendering images, video, and animations."),
        },
    },
    "Networking": {
        "Networking Basics": {
            "OSI Model": ("Open Systems Interconnection Model", "A conceptual framework for networking protocols in 7 layers."),
            "LAN": ("Local Area Network", "A network that spans a small geographical area."),
            "WAN": ("Wide Area Network", "A network that spans large geographical areas."),
        },
        "Cybersecurity Basics": {
            "Phishing": ("Fraudulent Communication", "A cyberattack using fake emails to steal sensitive information."),
            "Firewall": ("Network Security Device", "Monitors and controls incoming and outgoing network traffic."),
        },
    },
}

# Function to combine stacks from multiple topics or stacks
def combine_stacks(topic, stack_names):
    combined_stack = {}
    for stack_name in stack_names:
        if stack_name in topic:
            combined_stack.update(topic[stack_name])
    return combined_stack

# Global exit flag
exit_program = False

# Practice mode
def practice(stack):
    global exit_program
    questions = list(stack.keys())
    random.shuffle(questions)

    for question in questions:
        print(f"Question: {question}")
        user_input = input("Press Enter to reveal the answer: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting practice mode...")
            exit_program = True
            return

        meaning, definition = stack[question]
        print(f"Answer: {meaning}\nExplanation: {definition}\n")

    print("Practice session complete!")

def test(stack):
    global exit_program
    questions = list(stack.keys())
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)
    missed_questions = []

    # Initial test loop
    for question in questions:
        meaning, definition = stack[question]
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == 'exit':
            print("Exiting the quiz...")
            exit_program = True
            return

        if user_answer.strip().lower() == meaning.lower():
            print("Correct!")
            print(f"Explanation: {definition}\n")  # Show explanation if correct
            score += 1
        elif fuzz.ratio(user_answer.lower(), meaning.lower()) >= 80:
            print("Close enough!")
            print(f"Explanation: {definition}\n")  # Show explanation if close enough
            score += 1
        else:
            missed_questions.append(question)
            print("Incorrect...\n")

    # Summary of results
    print(f"\nYou got {score} out of {total_questions} correct.")

    # Retest missed questions once
    if missed_questions:
        print("\nReviewing missed questions:\n")
        for question in missed_questions:
            meaning, definition = stack[question]
            print(f"Question: {question}")
            user_answer = input("Your answer: ").strip()

            if user_answer.lower() == 'exit':
                print("Exiting the quiz...")
                exit_program = True
                return

            if user_answer.strip().lower() == meaning.lower():
                print("Correct!")
                print(f"Explanation: {definition}\n")  # Show explanation if correct
            else:
                print("Incorrect.")
                print(f"Answer: {meaning}")
                print(f"Explanation: {definition}\n")  # Show explanation if incorrect

# Program starts here
while not exit_program:
    print("\nAvailable topics:")
    for topic in flashcard_topics.keys():
        print(f"- {topic}")
    print("- Type 'exit' at any time")

    topic_name = input("\nEnter the topic name: ").strip()
    if topic_name.lower() == 'exit':
        print("Exiting the program...")
        break

    if topic_name not in flashcard_topics:
        print("Invalid topic. Please choose a valid topic.")
        continue

    selected_topic = flashcard_topics[topic_name]
    print(f"\nAvailable stacks in {topic_name}:")
    for stack_name in selected_topic.keys():
        print(f"- {stack_name}")
    print("- Random")

    stack_selection = input("\nEnter stack name(s) separated by commas: ").strip()
    if stack_selection.lower() == 'exit':
        print("Exiting the program...")
        break

    stack_names = [name.strip() for name in stack_selection.split(',')]

    if 'random' in [name.lower() for name in stack_names]:
        available_stacks = [stack for stack in selected_topic if stack not in stack_names]
        if available_stacks:
            random_stack = random.choice(available_stacks)
            print(f"Randomly selected stack: {random_stack}")
            stack_names.append(random_stack)

    stack_names = list(set(name for name in stack_names if name in selected_topic))
    if not stack_names:
        print("No valid stack names entered. Please try again.")
        continue

    combined_stack = combine_stacks(selected_topic, stack_names)

    print("\nSelect a mode:")
    print("Test")
    print("Practice")

    mode = input("Enter your choice (test/practice): ").strip().lower()
    if mode == 'test':
        test(combined_stack)
    elif mode == 'practice':
        practice(combined_stack)
    else:
        print("Invalid choice. Please select 'test' or 'practice'.")