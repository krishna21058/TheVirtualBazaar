# About Database creation and data insertion 

1. Database Schema and Integrity Constraints:-

A database schema is a structure that represents the logical storage
of the data in a database. It defines the tables, Columns, and
relationships between tables, as well as other objects such as views,
indexes and stored procedures. A schema is used to enforce
consistency and organization in a database, and provides a means
for users to understand the structure of the data stored in a database.
Integrity Constraints are sets of rules that ensures the accuracy and
consistency of data in a database. They are used to enforce rules
and to ensure that the data stored in a database adheres to certain
conditions. Eg. Primary Key include unique constraints, which enforce
unique values in a specific column and Foreign Key which enforces
relationships between tables. Integrity Constraints helps in preventing
data corruption and ensure that the data in the database in consistent
and accurate.

2. Data Population:-

In this we took the help of an online data Generator for SQL called
“Mockaroo” where we generated random unique data for different datatype
attributes of an entity of 100 rows



# Data Insertion Queries:


drop database if exists Dbmsproject;
CREATE DATABASE Dbmsproject;
use Dbmsproject;
CREATE TABLE Login (
Login_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Login_username VARCHAR(50) NOT NULL,
Password VARCHAR(40) ,
CHECK (LENGTH(Password) > 5),
Login_Type VARCHAR(30) NOT NULL
);


CREATE TABLE Customer (
Customer_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
FirstName VARCHAR(45) NOT NULL,
LastName VARCHAR(45) NOT NULL,
DOB DATE,
Age INT NOT NULL,
Street_number INT NOT NULL,
District VARCHAR(50) NOT NULL,
State VARCHAR(100) NOT NULL,
Pincode VARCHAR(100) DEFAULT NULL,
Phone VARCHAR(20) NOT NULL
);



CREATE TABLE Delivery_Person (
Delivery_person_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
FirstName VARCHAR(45) NOT NULL,
LastName VARCHAR(45) NOT NULL,
DOB DATE,
Age INT NOT NULL,
Gender VARCHAR(100) NOT NULL,
Address VARCHAR(150) NOT NULL,
Phone VARCHAR(20) NOT NULL
);



CREATE TABLE Retailer (
Retailer_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
FirstName VARCHAR(45) NOT NULL,
LastName VARCHAR(45) NOT NULL,
DOB DATE,
Age INT NOT NULL,
Address VARCHAR(50) NOT NULL,
Phone VARCHAR(20) NOT NULL
);



CREATE TABLE Category (
Category_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Category_name VARCHAR(50) NOT NULL
);



CREATE TABLE Product (
Product_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Product_category VARCHAR(225) NOT NULL,
Product_Availabilty BOOLEAN DEFAULT FALSE,
Product_price_in$ VARCHAR(100),
Product_name VARCHAR(120) NOT NULL,
Product_Discount INT
);




CREATE TABLE Cart (
Cart_Product_ID INT NOT NULL,
Cart_Customer_ID INT NOT NULL,
FOREIGN KEY (Cart_Product_ID) REFERENCES Product(Product_ID),
FOREIGN KEY (Cart_Customer_ID) REFERENCES Customer(Customer_ID)
);



CREATE TABLE Final_Order (
Order_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Order_Product_ID INT NOT NULL,
FOREIGN KEY (Order_Product_ID) REFERENCES Product(Product_ID),
Total_Charges VARCHAR(100),
Ordered_date DATE NOT NULL
);



CREATE TABLE Delivery (
Delivery_person_ID INT NOT NULL,
Delivery_Customer_ID INT NOT NULL,
Delivery_Order_ID INT NOT NULL,
FOREIGN KEY (Delivery_Customer_ID) REFERENCES
Customer(Customer_ID),
FOREIGN KEY (Delivery_Order_ID) REFERENCES Final_Order(Order_ID),
FOREIGN KEY (Delivery_person_ID) REFERENCES
Delivery_Person(Delivery_person_ID),
Date DATE NOT NULL
);



CREATE TABLE Store (
Store_Product_ID INT NOT NULL,
Store_Retailer_ID INT NOT NULL,
FOREIGN KEY (Store_Product_ID) REFERENCES Product(Product_ID),
FOREIGN KEY (Store_Retailer_ID) REFERENCES Retailer(Retailer_ID)
);



Indexes:
create index uname_index on login (Login_username);
create index login_type_index on login (Login_type);
create index retailer_fname_index on retailer(FirstName);
create index prod_name_index on product(Product_name);
create index del_person_fname_index on delivery_person(FirstName);
create index cat_name_index on category(category_name);
create index customer_fname_index on customer(FirstName)