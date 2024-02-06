import sqlite3 as sq

def ingresar_datos():
    nombre = input("Ingrese su nombre: ")
    numero_tarjeta = input("Ingrese su número de tarjeta: ")
    saldo = float(input("Ingrese su saldo actual: $"))

    try:
        conexion = sq.connect('cajero_del_Reservas.db')  # Establecer conexión a la BD
        cursor = conexion.cursor()                     # Creamos un cursor para trabajar con las consultas SQL  

        cursor.execute('''CREATE TABLE IF NOT EXISTS Saldo
                         (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT NOT NULL, NumeroTarjeta TEXT NOT NULL, Saldo REAL)''')

        cursor.execute("INSERT INTO Saldo (Nombre, NumeroTarjeta, Saldo) VALUES (?, ?, ?)", (nombre, numero_tarjeta, saldo))
        print("Datos ingresados correctamente.")

        conexion.commit()  # Hacemos commit para guardar los cambios en la BD

    except sq.Error as e:
        print("Error al ingresar los datos:", e)
    finally:
        cursor.close()
        conexion.close()  # Cerrar la conexión a la base de datos

# Llamamos a la función para ingresar datos
ingresar_datos()
