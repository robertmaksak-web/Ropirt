import sqlite3

connection = sqlite3.connect("para10_DB.sl3", 5)
cur = connection.cursor()
print(connection)
print(cur)
cur.execute("CREATE TABLE first_table (name TEXT);")
connection.commit()

connection.close()