"""

1. Let's Build Your Database: Your Gateway to Data Adventure!
mandatory
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
NOTE :

Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

Print error message to handle errors when failing to connect to the DB.

handle open and close of the DB in your script.

"""


import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values
import os

# # Load credentials
# config = dotenv_values(".env")

# try:
#     connection = mysql.connector.connect(
#         host=os.getenv('HOST'),
#         user=os.getenv('USER'),
#         password=os.getenv('PASSWORD')
#     )

#     if connection.is_connected():
#         cursor = connection.cursor()
#         cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
#         print("Database 'alx_book_store' created successfully!")
#         cursor.close()

# except mysql.connector.Error as err:
#     print("Failed creating database: {}".format(err))

# finally:
#     if connection.is_connected():
#         connection.close()





def create_database():
    try:
        # Connect to MySQL server (replace with your credentials)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            port="3306"
        )

        if mydb.is_connected():
            cursor = mydb.cursor()
            
            # Attempt to create the database using IF NOT EXISTS
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully or already exists.")
            
            # Close the cursor
            cursor.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

