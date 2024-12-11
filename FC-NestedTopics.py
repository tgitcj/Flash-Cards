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
        user_input = input("Press Enter to reveal the answer (or type 'exit' to quit): ").strip()

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
    print(f"\nAvailable stacks in {topic_name}:")
    for stack_name in selected_topic.keys():
        print(f"- {stack_name}")
    print("- Random (select a random stack)")

    stack_selection = input("\nEnter stack name(s) separated by commas, or type 'random': ").strip()
    if stack_selection.lower() == 'exit':
        print("Exiting the program...")
        break

    stack_names = [name.strip() for name in stack_selection.split(',')]

    if 'random' in [name.lower() for name in stack_names]:
        random_stack = random.choice(list(selected_topic.keys()))
        print(f"Randomly selected stack: {random_stack}")
        stack_names.append(random_stack)

    stack_names = list(set(name for name in stack_names if name in selected_topic))
    if not stack_names:
        print("No valid stack names entered. Please try again.")
        continue

    combined_stack = combine_stacks(selected_topic, stack_names)

    print("\nSelect a mode:")
    print("1. Test")
    print("2. Practice")

    mode = input("Enter your choice (1/2): ").strip()
    if mode == '1':
        test(combined_stack)
    elif mode == '2':
        practice(combined_stack)
    else:
        print("Invalid choice. Please select 1 or 2.")
