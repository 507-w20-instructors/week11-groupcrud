
import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()


cur.execute('SELECT COUNT(*) FROM Employee')
print(f"There are {cur.fetchone()[0]} employees.")

conn.close()
