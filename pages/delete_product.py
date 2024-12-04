import mysql.connector
from pages.home import sl

try:
    cnx = mysql.connector.connect(host="127.0.0.1", user="root",
                                  password="d4t4b4s3d3s1gn", db="pharmacy_store")
    cursor = cnx.cursor()

    product = sl.text_input("Product id: ")

    if sl.button("Submit"):
        if not product.isdigit() or int(product) <= 0:
            sl.error("IDs must be integers greater than 0.")
        else:
            cursor.execute('CALL delete_product(%s)',
                           [product])
            cursor.close()
            cnx.commit()
            cnx.close()
            sl.switch_page("pages/home.py")

except mysql.connector.Error as err:
    sl.error("Error: ", err)

if sl.button("Back"):
    sl.switch_page("pages/home.py")
