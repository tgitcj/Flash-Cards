import random

# Create a dictionary of IT acronyms
it_acronyms = {
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
}

def quiz():
    score = 0
    total_questions = len(it_acronyms)

    for acronym, meaning in it_acronyms.items():
        print(acronym)
        user_answer = input("Your answer: ")

        if user_answer.lower() == meaning.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The answer is:", meaning)

    print(f"You got {score} out of {total_questions} correct.")

quiz()