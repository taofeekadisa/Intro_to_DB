
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
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Details (

  orderdetailid INT NOT NULL,
  order_id INT,
  book_id INT,
  quantity DOUBLE,
  PRIMARY KEY (orderdetailid),
  FOREIGN KEY (order_id) REFERENCES Orders(order_id),
  FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
