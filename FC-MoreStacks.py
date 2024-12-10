import random
from fuzzywuzzy import fuzz

# Create a dictionary of flashcards, organized by stack
flashcard_stacks = {
    "IT Acronyms": {        
        "CPU": ("Central Processing Unit", "The CPU processes instructions from programs and manages data."),
        "RAM": ("Random Access Memory", "Temporary storage used by a computer to hold data and programs in use."),
        "HDD": ("Hard Disk Drive", "A traditional storage device with spinning disks to store data."),
        "SSD": ("Solid State Drive", "A faster storage device using flash memory."),
        "IP": ("Internet Protocol", "A set of rules for addressing and routing data across networks."),
        "DNS": ("Domain Name System", "Translates domain names into IP addresses."),
        "MAC": ("Media Access Control", "A unique identifier assigned to network interfaces."),
        "NIC": ("Network Interface Card", "Hardware for connecting a device to a network."),
        "BIOS": ("Basic Input Output System", "Firmware that initializes hardware during booting."),
        "RAID": ("Redundant Array of Independent Disks", "Data storage virtualization for performance and redundancy."),
    },

    "Hardware Components": {
        "Power Supply Unit": ("PSU", "Converts electrical power into usable power for internal components."),
        "Motherboard": ("Mainboard", "The main circuit board that connects all components."),
        "GPU": ("Graphics Processing Unit", "Handles rendering images, video, and animations."),
        "CMOS": ("Complementary Metal-Oxide-Semiconductor", "Stores BIOS settings and system time."),
        "Heat Sink": ("Cooling Component", "Dissipates heat from components like the CPU."),
    },

    "Networking Basics": {
        "OSI Model": ("Open Systems Interconnection Model", "A conceptual framework for networking protocols in 7 layers."),
        "LAN": ("Local Area Network", "A network that spans a small geographical area."),
        "WAN": ("Wide Area Network", "A network that spans large geographical areas."),
        "Ping": ("Packet Internet Groper", "A tool to test connectivity between two networked devices."),
        "Firewall": ("Network Security Device", "Monitors and controls incoming and outgoing network traffic."),
    },

    "Cybersecurity Basics": {
        "Phishing": ("Fraudulent Communication", "A cyberattack using fake emails to steal sensitive information."),
        "Firewall": ("Network Security Device", "Protects against unauthorized access to or from a private network."),
        "Antivirus": ("Malware Protection Software", "Detects and removes malicious software."),
        "Encryption": ("Data Protection Technique", "Converts data into a coded format to prevent unauthorized access."),
        "Two-Factor Authentication": ("2FA", "A security method that requires two forms of identity verification."),
    },

    "Troubleshooting Steps": {
        "Identify the Problem": ("First Step", "Gather information and identify the issue."),
        "Establish a Theory": ("Second Step", "Form a hypothesis about the root cause."),
        "Test the Theory": ("Third Step", "Verify the theory and identify the solution."),
        "Implement the Solution": ("Fourth Step", "Apply the fix and ensure it resolves the issue."),
        "Document the Results": ("Final Step", "Record the problem, solution, and process for future reference."),
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
        meaning, definition = combined_stack[question]
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == 'exit':
            print("Exiting the quiz...")
            return

        # First check for an exact match
        if user_answer.strip().lower() == meaning.lower():
            print("Correct!")
            print(f"Definition: {definition}")
            score += 1
        # Then check for a close enough match using fuzzy ratio
        elif fuzz.ratio(user_answer.lower(), meaning.lower()) >= 80:
            print("Correct! (Close enough)")
            print(f"Definition: {definition}")
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
            meaning, definition = combined_stack[question]
            print(question)
            user_answer = input("Your answer: ")

            if user_answer.lower() == 'exit':
                print("Exiting the quiz...")
                return

            # Repeat the same checks as above
            if user_answer.strip().lower() == meaning.lower():
                print("Correct!")
                print(f"Definition: {definition}")
            elif fuzz.ratio(user_answer.lower(), meaning.lower()) >= 80:
                print("Correct! (Close enough)")
                print(f"Definition: {definition}")
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
