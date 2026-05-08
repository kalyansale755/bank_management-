import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kalyan556",
    database="bank_system"
)

cursor = db.cursor()