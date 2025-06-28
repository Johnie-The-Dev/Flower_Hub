-- Create the database
CREATE DATABASE IF NOT EXISTS flowers_db;
USE flowers_db;

-- Create the flowers table
CREATE TABLE IF NOT EXISTS flowers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Create the transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    custname VARCHAR(100) NOT NULL,
    custid VARCHAR(50) NOT NULL,
    county VARCHAR(100) NOT NULL,
    town VARCHAR(100) NOT NULL,
    ftype VARCHAR(100) NOT NULL,
    nflowers INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    trans_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



USE flowers_db;

DELETE FROM transactions;
DELETE FROM flowers;



ALTER TABLE transactions AUTO_INCREMENT = 1;
ALTER TABLE flowers AUTO_INCREMENT = 1;