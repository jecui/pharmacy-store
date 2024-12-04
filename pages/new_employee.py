import mysql.connector
from numpy.f2py.auxfuncs import throw_error

from pages.home import sl

try:
    cnx = mysql.connector.connect(host="127.0.0.1", user="root",
                                  password="d4t4b4s3d3s1gn", db="pharmacy_store")
    cursor = cnx.cursor()

    first_name = sl.text_input("First name: ")
    last_name = sl.text_input("Last name: ")
    role = sl.radio("Role: ", ("Pharmacist", "Stock Manager", "Other"))
    if role == "Other":
        user_input = sl.text_input("Custom role: ")
    emer_cont = sl.text_input("Emergency contact: ")
    email = sl.text_input("Email: ")
    salary = sl.text_input("Salary: ")

    if sl.button("Submit"):
        try:
            if float(salary) <= 0 or salary == '':
                throw_error("Error: Salary must be greater than zero.")
        except ValueError as err:
            sl.error("Error: Invalid salary format.")
        else:
            if not emer_cont.isdigit() or int(emer_cont) <= 0:
                sl.error("Error: Invalid emergency contact number.")
            else:
                if role == "Other":
                    role = user_input
                cursor.execute('CALL new_employee(%s, %s, %s, %s, %s, %s)',
                                   (first_name, last_name, role, emer_cont, email, salary))
                cursor.close()
                cnx.commit()
                cnx.close()
                sl.switch_page("pages/home.py")

except mysql.connector.Error as err:
    sl.error("Error: ", err)

if sl.button("Back"):
    cnx.close()
    sl.switch_page("pages/home.py")
