import sqlite3

conexion = sqlite3.connect("bd1.db")

# Es demana a l'usuari que introdueixi un codi d'article.
codigo = int(input("Introdueix el codi d'un article: "))

# Es fa una consulta SELECT a la taula "articles" per a seleccionar la descripció i preu de l'article amb el codi introduït.
# Els resultats de la consulta es filtren per a mostrar només el registre amb el codi introduït.
# Els paràmetres de la consulta es passen com una tupla.
cursor = conexion.execute("select descripció,preu from articles where codi=?", (codigo,))

# Es recupera la primera fila del resultat de la consulta.
fila = cursor.fetchone()

# Si la fila no és buida, es mostra la descripció i el preu de l'article.
# Si la fila és buida, es mostra un missatge d'error.
if fila != None:
    print(fila)
else:
    print("No existeix un article amb aquest codi.")

# Es tanca la connexió a la base de dades.
conexion.close()
