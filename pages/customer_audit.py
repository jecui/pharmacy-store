import mysql.connector
from pages.home import sl

sl.title('Customer Audit Log')
try:
    cnx = mysql.connector.connect(host="127.0.0.1", user="root",
                                  password="d4t4b4s3d3s1gn", db="pharmacy_store")
    cursor = cnx.cursor()

    cursor.execute('CALL customer_audit_log()')
    customer_log = cursor.fetchall()
    columns = ["First name", "Last name", "Product", "Total price", "Amount", "Date"]
    sl.table([dict(zip(columns, row)) for row in customer_log])

    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    sl.error("Error: ", err)


if sl.button("Back"):
    cnx.close()
    sl.switch_page("pages/home.py")
