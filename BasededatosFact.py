import sqlite3 as sq

conect = sq.connect("Databass.db")
cursor = conect.cursor()

def table():
    cursor.execute('CREATE TABLE IF NOT EXISTS productos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio REAL)')
    cursor.close()
    conect.commit()
    conect.close()

table()