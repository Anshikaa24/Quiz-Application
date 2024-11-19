import os
#import hashlib

# File paths for storing quiz data, user data, and user scores
QUESTIONS_FILE = "questions.txt"
SCORES_FILE = "scores.txt"
USERS_FILE = "users.txt"

# Helper function to hash passwords
#def hash_password(password):
    #return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register_user():
    print("\n--- User Registration ---")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender (M/F): ")
    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")
    #hashed_password = hash_password(password)

    # Check if email already exists
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            for line in file:
                registered_email = line.strip().split("|")[5]
                if email == registered_email:
                    print("An account with this email already exists. Please login.\n")
                    return

    # Save user data
    with open(USERS_FILE, "a") as file:
        file.write(f"{name}|{age}|{gender}|{dob}|{phone}|{email}|{password}\n")
    print("Registration successful! You can now login.\n")

# Function to login an existing user
def login_user():
    print("\n--- User Login ---")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    # hashed_password = hash_password(password)

    # Validate login credentials
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                registered_email, registered_password = parts[5], parts[6]

                print(f"Comparing email: '{email}' == '{registered_email}'")
                print(f"Comparing password: '{password}' == '{registered_password}'")


                if email == registered_email and password == registered_password:
                    print(f"Login successful! Welcome, {parts[0]}.\n")
                    return parts[0]  # Return the user's name
        print("Invalid email or password. Please try again or register.\n")
        return None
    else:
        print("No users registered yet. Please register first.\n")
        return None

# Function to add quiz questions
def add_questions():
    print("\n--- Add Questions to the Quiz ---")
    while True:
        question = input("Enter the question: ")
        option_a = input("Enter option A: ")
        option_b = input("Enter option B: ")
        option_c = input("Enter option C: ")
        option_d = input("Enter option D: ")
        correct_answer = input("Enter the correct option (A/B/C/D): ").upper()

        # Append the question to the file
        with open(QUESTIONS_FILE, "a") as file:
            file.write(f"{question}|{option_a}|{option_b}|{option_c}|{option_d}|{correct_answer}\n")
        print("Question added successfully!\n")

        # Ask if the user wants to add another question
        more = input("Do you want to add another question? (yes/no): ").lower()
        if more != "yes":
            break

# Function to take the quiz
def take_quiz(user_name):
    if not os.path.exists(QUESTIONS_FILE):
        print("No questions available. Please add questions first.\n")
        return

    score = 0
    total_questions = 0

    with open(QUESTIONS_FILE, "r") as file:
        for line in file:
            total_questions += 1
            parts = line.strip().split("|")
            question, options, correct_answer = parts[0], parts[1:5], parts[5]

            # Display the question and options
            print(f"\nQ{total_questions}. {question}")
            print(f"A. {options[0]}")
            print(f"B. {options[1]}")
            print(f"C. {options[2]}")
            print(f"D. {options[3]}")

            # Get user answer
            user_answer = input("Your answer (A/B/C/D): ").upper()

            # Check if the answer is correct
            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}.\n")

    # Show the final score
    print(f"Quiz completed! Your score: {score}/{total_questions}")

    # Save the score
    with open(SCORES_FILE, "a") as file:
        file.write(f"{user_name}|{score}/{total_questions}\n")
    print("Your score has been recorded.\n")

# Function to view scores
def view_scores():
    if not os.path.exists(SCORES_FILE):
        print("No scores recorded yet.\n")
        return

    print("\n--- Leaderboard ---")
    with open(SCORES_FILE, "r") as file:
        for line in file:
            name, score = line.strip().split("|")
            print(f"{name}: {score}")
    print()

# Main menu
def main():
    while True:
        print("\n--- MCQ Quiz Application ---")
        print("1. Register")
        print("2. Login and Take Quiz")
        print("3. Add Questions")
        print("4. View Scores")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_name = login_user()
            if user_name:  # If login is successful
                take_quiz(user_name)
        elif choice == "3":
            add_questions()
        elif choice == "4":
            view_scores()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()



