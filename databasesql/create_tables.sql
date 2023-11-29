DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Orders;

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    product_price DECIMAL(10,2),
    product_quantity INT
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);