CREATE DATABASE smartphonesDatabase;
use smartphonesDatabase;

CREATE TABLE smartphones (
  smartphone_name VARCHAR(20),
  smartphone_id INT,
  smartphone_brand VARCHAR(100),
  smartphone_price FLOAT,
  smartphone_stock INT
);

CREATE TABLE users (
  username VARCHAR(20),
  pwd VARCHAR(20),
  userid INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY(userid)
);

CREATE TABLE orders (
  productId INT,
  userId INT,
  orderId INT
);

INSERT INTO smartphones (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
VALUES ("Iphone5", 1000, "Apple", 1600, 200);

INSERT INTO smartphones (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
VALUES ("Iphone5s", 1001, "Apple", 1800, 200);

INSERT INTO smartphones (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
VALUES ("Galaxy S20", 1002, "Apple", 2600, 200);

INSERT INTO smartphones (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
VALUES ("Galaxy S21", 1003, "Apple", 2800, 200);

INSERT INTO smartphones (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
VALUES ("Galaxy S22", 1004, "Apple", 2700, 200);

INSERT INTO smartphones (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
VALUES ("Galaxy S23", 1005, "Apple", 2870, 200);

INSERT INTO users (username, pwd)
VALUES ("gabi", "gabi");

INSERT INTO users (username, pwd)
VALUES ("admin", "admin");
