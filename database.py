
import mysql.connector
import configparser

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Extract MySQL credentials
db_config = {
    "host": config["mysql"]["host"],
    "user": config["mysql"]["user"],
    "password": config["mysql"]["password"],
}

def create_database():
    """Creates a MySQL database if it doesn't already exist."""
    try:
        # Connect to MySQL Server (without specifying a database)
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Define the database name
        db_name = config["mysql"]["database"]

        # Create the database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print(f"✅ Database '{db_name}' has been created or already exists.")

        # Close connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

if __name__ == "__main__":
    create_database()
