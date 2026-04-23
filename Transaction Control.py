import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO student VALUES(2,'Ram')")
    conn.commit()
except:
    conn.rollback()

conn.close()