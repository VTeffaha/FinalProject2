from menu import display_main_menu
from database import initialize_db
from voter import register_voter
from candidate import add_candidate, vote_for_candidate

def main():
    initialize_db()
    while True:
        choice = display_main_menu()
        if choice == '1':
            register_voter()
        elif choice == '2':
            add_candidate()
        elif choice == '3':
            vote_for_candidate()
        elif choice == '4':
            display_results()
        elif choice == '5':
            print("Thank you for using the Voting System!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

def display_main_menu() -> str:
    print("\n----- Voting System Menu -----")
    print("1. Register Voter")
    print("2. Add Candidate")
    print("3. Cast Vote")
    print("4. Display Results")
    print("5. Exit")
    return input("Enter your choice: ")

import sqlite3
from typing import List, Tuple

def initialize_db() -> None:
    conn = sqlite3.connect('data/votes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY,
            candidate_id INTEGER,
            FOREIGN KEY (candidate_id) REFERENCES candidates (id)
        )
    ''')
    conn.commit()
    conn.close()


from database import add_candidate_to_db, get_candidates

class Candidate:
    def __init__(self, name: str):
        self.name = name

def add_candidate() -> None:
    name = input("Enter candidate name: ")
    try:
        add_candidate_to_db(name)
        print(f"Candidate {name} added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Candidate already exists.")


