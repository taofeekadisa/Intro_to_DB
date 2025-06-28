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
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

from dotenv import dotenv_values

config = dotenv_values(".env")

cnx = mysql.connector.connect(user=config.get('USER'), 
                              password=config.get('PASSWORD'),
                              host=config.get('HOST'),
                              )

cursor = cnx.cursor()


try:
    if cnx.is_connected():
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print(" Database alx_book_store created successfully!")
except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
finally:
    cursor.close()
    cnx.close()



# def connect_database():
#     try:
#         if cnx.is_connected():
#             cursor = cnx.cursor()    
#             cursor.execute("USE alx_book_store")
#             print("Database alx_book_store connected successfully.")
#     except mysql.connector.Error as err:
#         print("Failed connecting to  database: {}".format(err))
#         exit(1)
        # print("Database alx_book_store does not exists.")
        # if err.errno == errorcode.ER_BAD_DB_ERROR:
        #     create_database(cursor, 'alx_book_store')
        #     print("Database alx_book_store created successfully.")
        #     cnx.database = 'alx_book_store'
        # else:
        #     print(err)
        #     exit(1)

# def close_connection():
#     cursor.close()
#     cnx.close()

# def main():
#     create_database()
#     # connect_database()
#     close_connection()

# if __name__ == "__main__":
#     create_database()

