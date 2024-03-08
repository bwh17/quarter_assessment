import sqlite3
import random

# ANSI escape codes for text color
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def get_categories():
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Fetch all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()

    # Close the connection
    conn.close()

    return [name[0] for name in table_names]

def get_random_question(category):
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()

    # Use lowercase category name as the table name
    table_name = category.lower()

    # Fetch a random question from the specified table
    cursor.execute(f"SELECT * FROM {table_name} ORDER BY RANDOM() LIMIT 1;")
    question = cursor.fetchone()

    # Close the connection
    conn.close()

    return question

def play_quiz_bowl():
    print("Welcome to Quiz Bowl!")

    # Get available categories
    categories = get_categories()

    if not categories:
        print("No categories found. Please check your database.")
        return

    print("Available Categories:", categories)

    # Let the user choose a category
    selected_category = input("Choose a category: ").capitalize()

    if selected_category not in categories:
        print("Invalid category. Please choose a valid category.")
        return

    print(f"\nCategory Selected: {selected_category}\n")

    # Get a random question from the selected category
    question = get_random_question(selected_category)

    if not question:
        print("No questions found for the selected category.")
        return

    # Display the question to the user
    print("Question:", question[1])  # Assuming the question is stored in the second column

    # Let the user input their answer
    user_answer = input("Your Answer: ")

    # Check if the answer is correct
    if user_answer.lower() == question[2].lower():  # Assuming the answer is stored in the third column
        print(GREEN + "Correct! Well done." + RESET)
    else:
        print(RED + f"Sorry, the correct answer is: {question[2]}" + RESET)

if __name__ == "__main__":
    play_quiz_bowl()