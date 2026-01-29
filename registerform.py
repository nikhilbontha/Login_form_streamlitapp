from random import choice
import streamlit as st
import pymysql

def create_database():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS registration_db;")
        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"Database creation failed: {e}")

def create_users_table():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="registration_db"
        )
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                surname VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                password VARCHAR(100)
            );
        """)
        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"Table creation failed: {e}")


# Ensure database and table exist
create_database()
create_users_table()


def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="registration_db"
    )
st.divider()

#form method to create a registration form for user input
menu = ["register","login"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "register":
    with st.form("register_form"):

        st.write("Please fill out the form:")
        name = st.text_input(" Name:")
        surname = st.text_input(" Surname:")
        email = st.text_input(" Email:")
        password = st.text_input(" Password:", type="password")

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                insert_query = """
                    INSERT INTO users (name, surname, email, password)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (name, surname, email, password))
                conn.commit()
                cursor.close()
                conn.close()
                st.success("Form submitted successfully! Data saved to database.")
            except Exception as e:
                st.error(f"Error: {e}")

elif choice == "login":
    with st.form("login_form"):
        st.write("Login Form:")
        email = st.text_input(" Email:")
        password = st.text_input(" Password:", type="password")
        login_button = st.form_submit_button("Login")
        if login_button:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                select_query = """
                    SELECT * FROM users WHERE email = %s AND password = %s
                """
                cursor.execute(select_query, (email, password))
                result = cursor.fetchone()
                cursor.close()
                conn.close()
                if result:
                    st.success("Login successful!")
                    st.balloons()
                    st.write("Welcome,", result[1])
                else:
                    st.error("Invalid email or password.")
            except Exception as e:
                st.error(f"Error: {e}")
st.divider()