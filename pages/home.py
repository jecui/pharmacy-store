import streamlit as sl

sl.title("Manage Your Pharmacy Store")

sl.header("Available actions:")

sl.subheader("See: ")
if sl.button("Customer Audit Log"):
    sl.switch_page("pages/customer_audit.py")

if sl.button("Store Audit Log"):
    sl.switch_page("pages/store_audit.py")

if sl.button("Inventory"):
    sl.switch_page("pages/inventory.py")

if sl.button("Prescription data"):
    sl.switch_page("pages/prescription.py")

sl.subheader("Update: ")
if sl.button("New employee"):
    sl.switch_page("pages/new_employee.py")

if sl.button("New order"):
    sl.switch_page("pages/new_order.py")

if sl.button("Add stock"):
    sl.switch_page("pages/add_stock.py")

if sl.button("Delete product"):
    sl.switch_page("pages/delete_product.py")