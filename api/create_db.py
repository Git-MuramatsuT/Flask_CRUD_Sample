import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    ''')

cursor.execute('''
    INSERT INTO todo (task) VALUES ('task1')
''')

cursor.execute('''
    INSERT INTO todo (task) VALUES ('task2')
''')

cursor.execute('''
    INSERT INTO todo (task) VALUES ('task3')
''')

conn.commit()

conn.close()