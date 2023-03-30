import sqlite3

conn = sqlite3.connect('mydb.db')
print("Successfully connected to database")

conn.execute("DELETE FROM mydb WHERE ID = 5; ")

conn.commit()
print("Successfully deleted last row")

conn.close()