"""

1. Let's Build Your Database: Your Gateway to Data Adventure!
mandatory
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
NOTE :

Required to print message such as Database 'alx_book_store' created successfully!
when database is successfully created.

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

DB_NAME = 'alx_book_store'

try:
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))
except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
    print("Database {} connected successfully.".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, DB_NAME)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
