import sqlite3

conexion = sqlite3.connect("bd1.db")

# Es demana a l'usuari que introdueixi un preu.
precio = float(input("Introdueix un preu: "))

# Es fa una consulta SELECT a la taula "articles" per a seleccionar la descripció dels articles amb un preu inferior al introduït.
# Els resultats de la consulta es filtren per a mostrar només els registres amb preu inferior al introduït.
# Els paràmetres de la consulta es passen com una tupla.
cursor = conexion.execute("select descripció from articles where preu<?", (precio,))

# Es recupera tots els resultats de la consulta amb el mètode `fetchall()` de l'objecte `cursor`.
filas = cursor.fetchall()

# Si hi ha resultats, es mostren les descripcions dels articles.
# Si no hi ha resultats, es mostra un missatge d'error.
if len(filas) > 0:
    for fila in filas:
        print(fila[0])
else:
    print("No hi ha articles amb preu inferior al introduït.")

# Es tanca la connexió a la base de dades.
conexion.close()
