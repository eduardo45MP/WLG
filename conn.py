# Import the mariadb module for connecting to the database
import mariadb

# Define a function to establish a database connection
def conn():
    # Database configuration details
    db_config = {
        "host": "localhost",     # Database host
        "user": "wordlists",     # Database username
        "password": "@123Change", # Database password
        "database": "wordlists"  # Database name
    }

    try:
        # Attempt to establish a connection using the provided configuration
        connection = mariadb.connect(**db_config)
        cursor = connection.cursor()

        print("Connected!")  # Print a message indicating successful connection
        return connection, cursor  # Return the connection and cursor objects
    except Exception as e:
        print("Error connecting database:", e)  # Print an error message if connection fails
        return None, None  # Return None values for connection and cursor