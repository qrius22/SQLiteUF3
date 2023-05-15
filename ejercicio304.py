import sqlite3

conexion = sqlite3.connect("bd1.db")

# Es realitzen tres insercions a la taula "articles" amb les dades "taronges", 23.50; "peres", 34 i "plàtans", 25.
# S'utilitza el mètode "execute()" de l'objecte "conexion" per a executar la sentència SQL i s'indiquen les dades amb una tupla.
conexion.execute("insert into articles(descripció,preu) values (?,?)", ("taronges", 23.50))
conexion.execute("insert into articles(descripció,preu) values (?,?)", ("peres", 34))
conexion.execute("insert into articles(descripció,preu) values (?,?)", ("plàtans", 25))

# S'ha de fer commit per a guardar els canvis a la base de dades.
conexion.commit()

# Es tanca la connexió a la base de dades
conexion.close()
