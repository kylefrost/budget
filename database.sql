CREATE DATABASE budget;

USE budget;

CREATE TABLE bills (
    bill_id INT NOT NULL AUTO_INCREMENT,
    bill_name VARCHAR(100),
    pay_date INT, -- Day of Month that payment is made
    pay_amount FLOAT,
    PRIMARY KEY (bill_id)
);

CREATE TABLE spending (
    spend_id INT NOT NULL AUTO_INCREMENT,
    spend_description VARCHAR(100),
    spend_date DATE,
    spend_amount FLOAT,
    account_used INT,
    PRIMARY KEY (spend_id)
);

CREATE TABLE accounts (
    account_id INT NOT NULL AUTO_INCREMENT,
    account_name VARCHAR(100),
    account_balance FLOAT,
    PRIMARY KEY (account_id)
);
