import mysql.connector

def get_db_connection():
    return mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="customer_management")

def add_customer(name, email, phone, address):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO customers (name, email, phone, address) VALUES (%s, %s, %s, %s)",(name, email, phone, address))
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
    cursor.execute("UPDATE customers SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s",(name, email, phone, address, customer_id))
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
