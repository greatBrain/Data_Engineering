CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    address_1 VARCHAR(25),
    address_2 VARCHAR(25),
    city VARCHAR(15),
    state VARCHAR(15),
    zip_code NUMERIC,
    join_date DATE
);

CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    product_code INT,
    product_description TEXT
);

CREATE TABLE transaction (
    transaction_id SERIAL PRIMARY KEY,
    transaction_date DATE NOT NULL DEFAULT CURRENT_DATE,
    product_id INT,
    customer_id INT,
    product_code INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id)
);