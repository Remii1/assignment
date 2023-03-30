import sqlite3

conn = sqlite3.connect('mydb.db')
print("Connected")

conn.execute("INSERT INTO mydb(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES (1,'Andrew','Allan',21,30000.00,'Manager')");
conn.execute("INSERT INTO mydb(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES (2,'Amelia','Roy',31,36000.00,'Manager')");
conn.execute("INSERT INTO mydb(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
               VALUES (3,'Faith','Smart',25,40000.00,'Manager')");
conn.execute("INSERT INTO mydb(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES (4,'Bernard','Zipporah',26,25000.00,'Manager')");
conn.execute("INSERT INTO mydb(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES (5,'Ryan','Aliyah',23,16000.00,'Manager')");
conn.commit()
print("Successfully inserted values in mydb table")

conn.close()