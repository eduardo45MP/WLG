# Import the necessary modules
import itertools  # For generating combinations of characters
from conn import conn  # Custom function to establish a database connection
import queue  # For creating a queue to store words
import threading  # For multithreading
from tqdm import tqdm  # For displaying a progress bar
import mariadb  # MariaDB database connector

# Define a class ProgressBar to manage and update the progress bar
class ProgressBar:
    def __init__(self, max_value):
        self.progress_bar = tqdm(total=max_value, desc="Inserting into database")

    def update(self):
        self.progress_bar.update(1)

    def close(self):
        self.progress_bar.close()

# Define a function to generate and insert a wordlist into the database using multithreading
def generate_and_insert_wordlist(table_name, characters, min_length, max_length, batch_size=1000):
    word_queue = queue.Queue()  # Create a queue to store generated words
    max_value = calculate_max_value(characters, min_length, max_length)  # Calculate the total number of words
    progress_bar = ProgressBar(max_value)  # Create a progress bar object

# Define a function to generate and insert a wordlist into the database using multithreading
def generate_and_insert_wordlist(table_name, characters, min_length, max_length, batch_size=1000):
    word_queue = queue.Queue()  # Create a queue to store generated words
    max_value = calculate_max_value(characters, min_length, max_length, batch_size)  # Calculate the total number of words
    progress_bar = ProgressBar(max_value)  # Create a progress bar object

    # Function to generate word combinations and insert them into the database
    def generate_and_insert():
        connection, cursor = conn()
        if connection:
            try:
                insert_query = f"INSERT INTO {table_name} (words) VALUES (%s);"
                for length in range(min_length, max_length + 1):
                    for combination in itertools.product(characters, repeat=length):
                        word = ''.join(combination)
                        try:
                            cursor.execute(insert_query, (word,))
                            connection.commit()  # Commit the changes to the database
                            progress_bar.update()  # Update the progress bar
                        except mariadb.IntegrityError as e:
                            if e.errno == 1062:  # ER_DUP_ENTRY
                                pass  # Ignore duplicate entries
                            else:
                                raise  # Raise an exception for other errors
                progress_bar.close()  # Close the progress bar
                print("Process completed.")  # Print a completion message
            except Exception as e:
                print("Error inserting wordlist:", e)
            finally:
                cursor.close()
                connection.close()

    # Create a thread to generate and insert words
    insert_thread = threading.Thread(target=generate_and_insert)

    # Start the thread
    insert_thread.start()

    # Wait for the thread to finish
    insert_thread.join()

# Define a function to calculate the maximum number of words based on characters and length
def calculate_max_value(characters, min_length, max_length, batch_size):
    max_value = 0
    for length in range(min_length, max_length + 1):
        max_value += len(characters) ** length

    # Adjust max_value based on batch_size
    max_value = max_value // batch_size * batch_size
    return max_value


# New function to perform batch insert
def insert_batch(cursor, query, data):
    placeholders = ', '.join(['%s'] * len(data))
    query = query % placeholders
    cursor.execute(query, [item for sublist in data for item in sublist])
