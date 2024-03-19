import sqlite3 as sq

conn = sq.connect("Databass.db")
c = conn.cursor()

productoK = input("Ingrese el código del producto: ")

producto = c.execute(f"SELECT * FROM Productos WHERE id='{productoK}'").fetchone()
if producto is None:
    print("No se encontró el producto.")
else:
    print(f"""\nCódigo: {producto[0]}
Nombre: {producto[1]}
Precio: ${producto[2]}\n""")
    
                   