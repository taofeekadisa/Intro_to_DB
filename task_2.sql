"""

2. Create Your Magical Tables
mandatory
Write a script that creates all the tables below in alx_book_store in your MySQL server.

Tables

For each table/relation below, you can find the attributes in task 0
books
authors
customers
orders
order details
Name of the file should be task_2.sql

All SQL keywords should be in uppercase

"""

CREATE TABLE Authors (
  author_id INT NOT NULL,
  author_name VARCHAR(215),
  PRIMARY KEY (author_id)
);

CREATE TABLE Books (
  book_id INT NOT NULL,
  title VARCHAR(130),
  author_id INT,
  price DOUBLE,
  publication_date DATE,
  PRIMARY KEY (book_id),
  FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE  Customers (
  customer_id INT NOT NULL,
  customer_name VARCHAR(215),
  email VARCHAR(215),
  address TEXT,
  PRIMARY KEY (customer_id)
);


CREATE TABLE Orders (
  order_id INT NOT NULL,
  customer_id INT,
  order_date DATE,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
);