import pyodbc
import random

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-76NBGCK\SQLEXPRESS'
DATABASE_NAME = 'trial_database'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = pyodbc.connect(connection_string)
print("Succes",conn)

cursor = conn.cursor()

ıd = random.randint(0,100)
name = input("Name :")
phone_number = input("Phone_Number :")

sql_query = 'INSERT INTO users (ıd ,name, phone_number) VALUES (?,?,?)'
cursor.execute(sql_query, (ıd ,name, phone_number))
conn.commit()

conn.close()

# birden fazla özellik ekle 

# tkinter ile bir arayüz ekleyebilirsin
