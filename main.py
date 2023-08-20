# Import the necessary modules
import queue
import threading
from setting import create_wordlist_table
from gen import generate_and_insert_wordlist

# Define the main function
def main():
    # Print a welcome message
    print("Welcome to Wordlist Generator!")

    # Prompt the user for input
    table_name = input("Enter the name of the wordlist table: ")
    characters = input("Enter the characters to include in the words: ")
    min_length = int(input("Enter the minimum word length: "))
    max_length = int(input("Enter the maximum word length: "))

    # Remove spaces from the characters string
    #characters = characters.replace(" ", "")

    # Call the create_wordlist_table function to create the table in the database
    create_wordlist_table(table_name)

    # Call the generate_and_insert_wordlist function to generate and insert the wordlist into the database
    generate_and_insert_wordlist(table_name, characters, min_length, max_length)

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the wordlist generation process
