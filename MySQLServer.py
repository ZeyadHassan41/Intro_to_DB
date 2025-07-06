import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # <- change this to your actual root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        # Close cursor and connection properly
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
