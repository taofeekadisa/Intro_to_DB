
import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values
import os

# Load credentials
config = dotenv_values(".env")

try:
    connection = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD')
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))

finally:
    cursor.close()
    if connection.is_connected():
        connection.close()




