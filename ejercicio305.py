import sqlite3

conexion = sqlite3.connect("bd1.db")

# Es fa una consulta SELECT a la taula "articles" per a seleccionar totes les files i columnes.
# El mètode "execute()" de l'objecte "conexion" s'utilitza per a executar la consulta SQL.
# Els resultats de la consulta es guarden en l'objecte "cursor".
cursor = conexion.execute("select codigo,descripció,preu from articles")

# S'utilitza un bucle "for" per a recórrer les files de la consulta i es mostra cada fila amb el mètode "print()".
# Cada fila es tracta com a una tupla, amb les dades de cada columna.
for fila in cursor:
    print(fila)

# Es tanca la connexió a la base de dades.
conexion.close()
