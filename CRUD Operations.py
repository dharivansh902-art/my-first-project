import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO student VALUES(1,'Shivam')")
cursor.execute("SELECT * FROM student")

print(cursor.fetchall())

conn.commit()
conn.close()