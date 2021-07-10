import sqlite3

try:
    conn = sqlite3.connect('Vidhi.db')
    create_table_query = '''CREATE TABLE doctors (
                                name TEXT NOT NULL,
                                port text NOT NULL,
                                insurance text NOT NULL,
                                cost INTEGER);'''

    cursor = conn.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(create_table_query)
    conn.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (conn):
        conn.close()
        #print("sqlite connection is closed")
