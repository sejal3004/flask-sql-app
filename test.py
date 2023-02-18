import sqlite3
print("library imported")

print("creating connection")

conn = sqlite3.connect('mydb1.db')
conn.close()

print("\n The SQLITE db connection is created and closed")