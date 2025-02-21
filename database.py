
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

# Define the database name
DB_NAME = config["mysql"]["database"]

# Define table schema
TABLES = {}
TABLES["logs"] = (
    "CREATE TABLE IF NOT EXISTS logs ("
    "   id INT(11) NOT NULL AUTO_INCREMENT,"
    "   text VARCHAR(250) NOT NULL,"
    "   user VARCHAR(250) NOT NULL,"
    "   created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "   PRIMARY KEY (id)"
    ") ENGINE=InnoDB;"
)

def create_database():
    """Creates a MySQL database if it doesn't already exist."""
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print(f"✅ Database '{DB_NAME}' has been created or already exists.")
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

def create_tables():
    """Creates the necessary tables in the database."""
    try:
        db_config["database"] = DB_NAME  # Add database to connection config
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(f"USE {DB_NAME};")

        for table_name, table_sql in TABLES.items():
            cursor.execute(table_sql)
            print(f"✅ Table '{table_name}' has been created or already exists.")

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

if __name__ == "__main__":
    create_database()
    create_tables()
