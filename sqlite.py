import sqlite3

con = sqlite3.connect("example.db")
cur = con.cursor()
# cur.execute('CREATE TABLE movie(title, year, score)')
# cur.execute("INSERT INTO movie VALUES('1', 'Inception', 2010, 8.8)")
# cur.execute("INSERT INTO movie VALUES('', 'The Matrix', 1999, 8.7)")
# cur.execute("INSERT INTO movie VALUES('', 'Interstellar', 2014, 8.6)")
# cur.execute("DROP TABLE movie")
# res = cur.execute("SELECT/ ")
# print(res.fetchall())
con.commit()
con.close()