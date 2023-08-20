# Import the conn function from the conn module
from conn import conn

# Define a function to create a wordlist table in the database
def create_wordlist_table(table_name):
    # Establish a database connection using the conn function
    connection, cursor = conn()

    # Check if the connection is established successfully
    if connection:
        try:
            # SQL query to create a new table if it doesn't exist
            create_table_query = f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    words TEXT NOT NULL UNIQUE
                );
            '''
            # Execute the create table query
            cursor.execute(create_table_query)
            print("Table created successfully.")  # Print a success message
        except Exception as e:
            print("Error creating the table:", e)  # Print an error message if table creation fails
        finally:
            cursor.close()      # Close the cursor
            connection.close()  # Close the connection

# Call the function to create the table if this script is run as the main program
if __name__ == "__main__":
    table_name = 'teste'  # Set the table name as 'teste'
    create_wordlist_table(table_name)  # Call the create_wordlist_table function with the specified table name
