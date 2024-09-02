import streamlit as st
from backend import add_customer, get_customers, update_customer, delete_customer

st.title("Customer Management System")

menu = ["Add Customer", "View Customers", "Update Customer", "Delete Customer"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Customer":
    st.image("https://media.licdn.com/dms/image/C5612AQEXTt4grfiTxQ/article-cover_image-shrink_720_1280/0/1520181045312?e=2147483647&v=beta&t=Z6g_nFW524kw9hTrqMfS9CshPF4-VV4OffMyJmROOCI")
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
