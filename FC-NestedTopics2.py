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

# Test mode
def test(stack):
    global exit_program
    questions = list(stack.keys())
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)
    missed_questions = []

    for question in questions:
        meaning, definition = stack[question]
        print(question)
        user_answer = input("Your answer (or type 'exit' to quit): ").strip()

        if user_answer.lower() == 'exit':
            print("Exiting the quiz...")
            exit_program = True
            return

        if user_answer.strip().lower() == meaning.lower():
            print("Correct!")
        elif fuzz.ratio(user_answer.lower(), meaning.lower()) >= 80:
            print("Correct! (Close enough)")
        else:
            missed_questions.append(question)
            print("Incorrect.")

    print(f"\nYou got {score} out of {total_questions} correct.")

    if missed_questions:
        print("\nLet's try the missed questions again.")
        for question in missed_questions:
            meaning, definition = stack[question]
            print(question)
            user_answer = input("Your answer (or type 'exit' to quit): ").strip()

            if user_answer.lower() == 'exit':
                print("Exiting the quiz...")
                exit_program = True
                return

            if user_answer.strip().lower() == meaning.lower():
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is: {meaning}")

# Program starts here
while not exit_program:
    print("\nAvailable topics:")
    for topic in flashcard_topics.keys():
        print(f"- {topic}")
    print("- Exit")

    topic_name = input("\nEnter the topic name: ").strip()
    if topic_name.lower() == 'exit':
        print("Exiting the program...")
        break

    if topic_name not in flashcard_topics:
        print("Invalid topic. Please choose a valid topic.")
        continue

    selected_topic = flashcard_topics[topic_name]
    selected_stacks = []  # Keep track of selected stacks
    while True:
        print(f"\nAvailable stacks in {topic_name}:")
        for stack_name in selected_topic.keys():
            if stack_name not in selected_stacks:
                print(f"- {stack_name}")
        print("- Random")

        stack_selection = input("\nEnter stack name(s) separated by commas, or type 'random': ").strip()
        if stack_selection.lower() == 'exit':
            print("Exiting the program...")
            exit_program = True
            break

        stack_names = [name.strip() for name in stack_selection.split(',')]

        if 'random' in [name.lower() for name in stack_names]:
            available_stacks = [stack for stack in selected_topic.keys() if stack not in selected_stacks]
            if available_stacks:
                random_stack = random.choice(available_stacks)
                print(f"Randomly selected stack: {random_stack}")
                stack_names.append(random_stack)
            else:
                print("No additional stacks available for random selection.")
                continue

        stack_names = [name for name in stack_names if name in selected_topic and name not in selected_stacks]
        if not stack_names:
            print("No valid or new stack names entered. Please try again.")
            continue

        selected_stacks.extend(stack_names)
        combined_stack = combine_stacks(selected_topic, selected_stacks)

        print("\nSelect a mode:")
        print("1. Test")
        print("2. Practice")

        mode = input("Enter your choice (1/2): ").strip()
        if mode == '1':
            test(combined_stack)
            break
        elif mode == '2':
            practice(combined_stack)
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
