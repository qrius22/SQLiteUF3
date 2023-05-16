import sqlite3

# S'estableix una connexió a la base de dades anomenada "bd1.db"
conexion = sqlite3.connect("bd1.db")

try:
    # S'intenta crear una taula anomenada "articles" amb tres camps:
    # "codi" (enter, clau primària i autoincremental), 
    # "descripció" (text) i "preu" (real)
    conexion.execute("""create table articles (
                              codi integer primary key autoincrement,
                              descripció text,
                              preu real
                        )""")
    # Si es crea la taula sense problemes, es mostra un missatge a pantalla indicant que s'ha creat la taula "articles"
    print("s'ha creat la taula articles")                        
except sqlite3.OperationalError:
    # Si no es pot crear la taula (perquè ja existeix), es mostra un missatge a pantalla indicant que la taula "articles" ja existeix
    print("La taula articles ja existeix")                    

# Es tanca la connexió a la base de dades
conexion.close()
