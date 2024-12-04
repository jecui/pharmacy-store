import mysql.connector
import streamlit as sl

name = sl.text_input("Username:")
password = sl.text_input("Password:")

if sl.button("Sign in"):
    try:
        mysql.connector.connect(host="Jennifers-MacBook-Pro.local", user=name,
                                  password=password, db="pharmacy_store", port = 3306)
    except mysql.connector.Error as err:
        sl.error("Wrong username or password. Try again.")
    else:
        sl.switch_page("pages/home.py")