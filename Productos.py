import random as rm
import sqlite3 as sq

conn = sq.connect("Databass.db")
cursor = conn.cursor()
productoKey = rm.randint(1, 20000)
producto = input("Ingrese el nombre del producto: ")
precio = int(input("Precio del prducto: "))

def insert():
    cursor.execute('INSERT INTO productos VALUES(?, ?, ?)', (productoKey, producto, precio))

    cursor.close()
    conn.commit()
    conn.close()

insert()