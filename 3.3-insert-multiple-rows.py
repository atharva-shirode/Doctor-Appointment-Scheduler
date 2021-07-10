
import sqlite3

def insertMultiData(recordList):
    try:
        conn = sqlite3.connect('Vidhi.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        insert_query = """INSERT INTO doctors
                          (name, port, insurance, cost) 
                          VALUES (?, ?, ?, ?);"""

        cursor.executemany(insert_query, recordList)
        conn.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into availabilities table")
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

recordsToInsert = [('doc1', '41000', 'insurance1',30),
                   ('doc1', '41000', 'insurance2',20),
                   ('doc1', '41000', 'insurance3',50),
                   ('doc2', '42000', 'insurance1',40),
                   ('doc2', '42000', 'insurance2',60),
                   ('doc2', '42000', 'insurance2',10)]

insertMultiData(recordsToInsert)
