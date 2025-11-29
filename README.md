A structured, menu-driven Inventory Management System designed to handle Products, Purchases, Sales, and Users.
This project is built in Python with a MySQL backend and follows a simplified BRD-style structure for clarity, maintainability, and future enhancements.
1. Purpose & Scope

The system provides core inventory operations:

-In Scope
--Product lifecycle management (add/update/delete/search)
--Purchase order creation and listing
--Sales recording with auto stock deduction
--Basic user management
--Automated MySQL table creation and setup

-Out of Scope (Future Enhancements)
--GUI or web interface
--Authentication/role-based access
--Reporting dashboards
--Password hashing

2. System Overview

The application follows a menu-driven workflow implemented in Python.
All data is stored in a MySQL database using structured, normalized tables.

Key design highlights:

-3NF-compliant schema
-Foreign-key–based relations
-Secure parameterized SQL queries
-Clear modular flow: Product → Purchase → Sales → Users
-Uses datetime-based unique IDs (can be upgraded to AUTO_INCREMENT)

3. Database Design (3NF)
Tables:
-product(pcode PK, pname, price, pqty, pcat)
-orders(orderid PK, orderdate, pcode FK, pprice, pqty, supplier, pcat)
-sales(salesid, salesdate, pcode FK, pprice, pqty, total)
-user(uid PK, uname, upwd)

Normalization Summary:

1NF: Atomic fields, no repeating groups
2NF: All attributes depend fully on primary keys
3NF: No transitive dependencies
Exception: category duplicated in orders (intentional denormalization for faster queries)

4. Installation & Setup
Step 1 — Clone the repository

git clone https://github.com/<your-username>/inventory-management.git
cd inventory-management

Step 2 — Install dependencies

pip install -r requirements.txt


Step 3 — Create database in MySQL

CREATE DATABASE stock;

Step 4 — Set environment variables

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=stock

Step 5 — Run the script

python inventory.py

5. Functional Workflow Summary
-Product Module
--Add product
--Update stock
--Delete product
--Search by code/category
--List all products

-Purchase Module
--Generate order with supplier & category
--Timestamp-based OrderID
--List orders
--Sales Module
--Record sale
--Auto stock deduction
--Calculate bill total
--List sales

-User Module
--Add user
--List users