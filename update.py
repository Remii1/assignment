import sqlite3

conn = sqlite3.connect('mydb.db')
print("Successfully connected to database")

conn.execute("UPDATE mydb set FIRSTNAME = 'Faith' WHERE ID = 1; ")

conn.commit()
print("Successfully updated")

conn.close()