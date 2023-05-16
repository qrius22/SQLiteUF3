import sqlite3
import os


def check_db(filename):
    return os.path.exists(filename)


def display_table(conn):
    cursor = conn.cursor()
    cursor.execute('select name, size, date from images;')
    for name, size, date in cursor.fetchall():
        print(name, size, date)


#conn = sqlite3.connect('database.db')
#conn = sqlite3.connect(':memory:')
#db_file = 'database.db'
#with sqlite3.connect(db_file) as conn:
#    print('Created the connection!')
#print('Automatically closed the connection!')
#c = conn.cursor()

db_file = 'database.db'

schema_file = 'schema.sql'



if check_db(db_file):
    print('Database already exists. Exiting...')
    exit(0)


with open(schema_file, 'r') as rf:
    schema = rf.read()


with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
    
    conn.executescript(schema)
    print('Created the Table! Now inserting')

    conn.executescript("""
                       insert into images (name, size, date)
                       values
                       ('sample.png', 100, '2019-10-10'),
                       ('ask_python.png', 450, '2019-05-02'),
                       ('class_room.jpeg', 1200, '2018-04-07');
                       """)
    print('Inserted values into the table!')

    cursor = conn.cursor()

    cursor.execute("""
                      select * from images
                      """)

    for row in cursor.fetchall():
        name, size, date = row
        print(f'{name} {size} {date}')
print('Closed the connection!')


db_filename = 'database.db'


with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    display_table(conn1)
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into images (name, size, date)
    values
    ('JournalDev.png', 2000, '2020-02-20');
    """)

    print('\nAfter changes in conn1:')
    display_table(conn1)

    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

    
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        display_table(conn3)

    cursor1.execute("""
    insert into images (name, size, date)
    values ('Hello.png', 200, '2020-01-18');
    """)

    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)


    conn1.rollback()
    print('\nAfter connection 1 rollback:')
    with sqlite3.connect(db_filename) as conn4:
        display_table(conn4)