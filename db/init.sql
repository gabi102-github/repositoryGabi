CREATE DATABASE smartphonesDatabase;
use smartphonesDatabase;

CREATE TABLE smartphones (
  smartphone_name VARCHAR(20),
  smartphone_id INT,
  smartphone_brand VARCHAR(100),
  smartphone_price FLOAT,
  smartphone_stock INT
);

INSERT INTO Products (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
VALUES ("Iphone 5", 1000, "Apple", 1600, 200);

INSERT INTO Products (smartphone_name, smartphone_id, smartphone_brand, smartphone_price, smartphone_stock)
VALUES ("Iphone 5s", 1001, "Apple", 1800, 200);
