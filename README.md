# Customer-Management
Project: Customer Management System
Overview
Why
Customer management is crucial for businesses to maintain strong relationships with their clients, streamline processes, and improve customer satisfaction. A well-organized Customer Management System (CMS) allows businesses to store, retrieve, and manage customer data efficiently, leading to better customer service and informed decision-making.
What
The Customer Management System is a software solution designed to handle customer-related information. It includes functionalities for adding, updating, and viewing customer records. The system will use MySQL for database management, Python for backend operations, and Streamlit for the user interface. Key features will include:
•	Adding new customers
•	Viewing customer details
•	Updating existing customer information
•	Deleting customer records
How
1.	Database Setup (MySQL)
o	Design and create the database schema.
o	Implement tables for storing customer information.
2.	Backend Development (Python)
o	Develop functions to interact with the database (CRUD operations).
o	Ensure secure and efficient data handling.
3.	Frontend Development (Streamlit)
o	Create a user-friendly interface for interacting with the system.
o	Integrate frontend with the backend to provide real-time data updates.
Step-by-Step Implementation
1. Database Setup (MySQL)
a. Install MySQL: Ensure MySQL is installed and running on your system.
b. Create a Database:
sql
CREATE DATABASE customer_management;
c. Create a Customer Table:
sql
USE customer_management;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 
2. Backend Development (Python)
a. Install Required Packages:
pip install mysql-connector-python streamlit
b. Database Connection Backend CRUD:
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="customer_management"
    )

def add_customer(name, email, phone, address):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO customers (name, email, phone, address) VALUES (%s, %s, %s, %s)",
                   (name, email, phone, address))
    db.commit()
    cursor.close()
    db.close()

def get_customers():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

def update_customer(customer_id, name, email, phone, address):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE customers SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s",
        (name, email, phone, address, customer_id)
    )
    db.commit()
    cursor.close()
    db.close()

def delete_customer(customer_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM customers WHERE id=%s", (customer_id,))
    db.commit()
    cursor.close()
    db.close()
4.	Frontend Development (Streamlit) 

 
  
 
a. Create a Streamlit App:
python:

import streamlit as st
from backend import add_customer, get_customers, update_customer, delete_customer

st.title("Customer Management System")

menu = ["Add Customer", "View Customers", "Update Customer", "Delete Customer"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Customer":
    st.subheader("Add New Customer")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    address = st.text_area("Address")
    if st.button("Add Customer"):
        add_customer(name, email, phone, address)
        st.success("Customer added successfully")

elif choice == "View Customers":
    st.subheader("Customer List")
    customers = get_customers()
    for customer in customers:
        st.write(f"ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}, Phone: {customer[3]}, Address: {customer[4]}")

elif choice == "Update Customer":
    st.subheader("Update Customer")
    customer_id = st.number_input("Customer ID", min_value=1)
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    address = st.text_area("Address")
    if st.button("Update Customer"):
        update_customer(customer_id, name, email, phone, address)
        st.success("Customer updated successfully")

elif choice == "Delete Customer":
    st.subheader("Delete Customer")
    customer_id = st.number_input("Customer ID", min_value=1)
    if st.button("Delete Customer"):
        delete_customer(customer_id)
        st.success("Customer deleted successfully")
Conclusion
We can build a functional Customer Management System using MySQL, Python, and Streamlit. This system will enable us to efficiently manage customer data, enhancing overall business processes and customer satisfaction.

