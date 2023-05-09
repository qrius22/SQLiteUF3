import sqlite3

conexion=sqlite3.connect("bd1.db")
precio=float(input("Ingrese un precio:"))
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))
filas=cursor.fetchall()
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
conexion.close()