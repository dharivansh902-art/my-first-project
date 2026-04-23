import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE student(id INT, name TEXT)")

conn.commit()
conn.close()