import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            deadline DATE NOT NULL
        )
    ''')

cursor.execute('''
    INSERT INTO todo (task, deadline) VALUES ('task1', '2024-01-01')
''')

cursor.execute('''
    INSERT INTO todo (task, deadline) VALUES ('task2', '2024-02-01')
''')

cursor.execute('''
    INSERT INTO todo (task, deadline) VALUES ('task3', '2024-03-01')
''')

conn.commit()

conn.close()