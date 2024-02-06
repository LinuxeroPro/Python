import sqlite3 as sq

def revisar_saldo(cursor):
    try:
        cursor.execute("SELECT * FROM Saldo WHERE ID=1;")   # Consulta que devuelve todos los registros de la tabla 'Saldo' y
        saldo_data = cursor.fetchone()                        # Obtiene el primer registro de la consulta anterior
        
        if saldo_data is not None:
            print("\n Su nombre es ", saldo_data[1])               # Imprime el dato [0] (Nombre)
            print(" Su número de tarjeta es ", saldo_data[2])       # Imprime el dato [1] (NumeroTarjeta)
            print(" Su saldo actual es de $", saldo_data[3], "\n")         # Imprime el dato [2] (Saldo)
        else:
            print("No se encontraron datos de saldo.")
            
    except sq.Error as e:
        print("Error al recuperar los datos de saldo:", e)

def modificar_saldo(cursor, monto, tipo_transaccion):
    print("Modificando saldo...")
    print("Monto:", monto)
    print("Tipo de transacción:", tipo_transaccion)
    try:
        cursor.execute("SELECT * FROM Saldo WHERE ID=1;")   # Obtener el registro de saldo
        saldo_data = cursor.fetchone()
        
        if saldo_data is not None:
            saldo_actual = saldo_data[3]  # Obtener el saldo actual
            
            if tipo_transaccion.lower() == "depositar":
                nuevo_saldo = saldo_actual + monto
            elif tipo_transaccion.lower() == "retirar":
                if monto <= saldo_actual:
                    nuevo_saldo = saldo_actual - monto
                else:
                    print("Saldo insuficiente para realizar el retiro.")
                    return
            else:
                print("Tipo de transacción no válido.")
                return

            # Actualizar el saldo en la base de datos
            cursor.execute("UPDATE Saldo SET Saldo=? WHERE ID=1", (nuevo_saldo,))
            print("Saldo actualizado correctamente.")
            print("Nuevo saldo: $", nuevo_saldo)

            # Realizar el commit para guardar los cambios en la base de datos
            conexion.commit()
            
            return nuevo_saldo
        else:
            print("No se encontraron datos de saldo.")
    except sq.Error as e:
        print("Error al modificar el saldo:", e)


print("             Bienvenido al cajero del Reservas")
print("      ¿Qué tipo de transacción desea hacer el día de hoy? \n")
print(" Depositar dinero en la cuenta \n Retirar dinero de la cuenta \n")
opcion1 = input(": ")

if opcion1 == "Depositar":
    print("Ingrese la cantidad a ingresar:")
    monto = float(input())
    tipo_transaccion = "depositar"
elif opcion1 == "Retirar":
    print("Cuánto dinero quiere retirar?: ")
    monto = float(input(""))
    tipo_transaccion = "retirar"
else:
    print("Opcion incorrecta, vuelva a intentarlo.")

# Abrimos la base de datos y creamos una tabla si no existe.
conexion = sq.connect('cajero_del_Reservas.db')  # Establecer conexión a la BD
cursor = conexion.cursor()                     # Creamos un cursor para trabajar con las consultas SQL  

try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS Transacciones
                     (ID INTEGER PRIMARY KEY AUTOINCREMENT, Fecha DATE NOT NULL, TipoTransaccion TEXT NOT NULL, Monto REAL)''')
except sq.Error as error:
    print("Error al crear la tabla", error)

try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS Saldo
                     (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT NOT NULL, NumeroTarjeta TEXT NOT NULL, Saldo REAL)''')
except sq.Error as error:
    print("Error al crear la tabla Saldo:", error)

try:
    cursor.execute("INSERT INTO Transacciones (Fecha, TipoTransaccion, Monto) VALUES (date('now'), ?, ?)", (opcion1, monto))
    print("La transacción ha sido registrada correctamente.")
except sq.IntegrityError as e:
    print("Error al insertar la transacción:", e)

# Modificar el saldo
if opcion1 == "Depositar" or opcion1 == "Retirar":
    modificar_saldo(cursor, monto, tipo_transaccion)

# Función para revisar el saldo
print("¿Desea revisar su saldo?")
opcion2 = input("Si/No : ")
if opcion2 == "Si":
    revisar_saldo(cursor)

# Cerramos la conexión a la Base de Datos
cursor.close()
conexion.close()