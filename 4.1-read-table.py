
import sqlite3

def readTable():
    try:
        conn = sqlite3.connect('Vidhi.db')
        cursor = conn.cursor()
        #print("Connected to SQLite")

        select_query = """SELECT * from doctors"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        #print("Total rows are:  ", len(records))
        #print("Printing each row")
        '''for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1]) 
            print("Email: ", row[2])
            print("JoiningDate: ", row[3])
            print("Salary: ", row[4],end="\t")
            print("\n")
        '''
        print("Name: ",end="\t")
        print("Port: ",end="\t") 
        print("Insurance: ",end="\t")
        print("Cost: ",end="\t")
        #print("Port: ", end="\t")
        print("\n")
        for r in records:
            print(r[0],end="\t")
            print(r[1],end="\t") 
            print(r[2],end="\t")
            print(r[3],end="\t\t")
            #print(r[4],end="\t")
            print("\n")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            #print("The SQLite connection is closed")

readTable()
