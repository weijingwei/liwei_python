import sqlite3


con = sqlite3.connect('d:/mydatabase.db')
cur = con.cursor()
cur.execute('CREATE TABLE foo (o_id INTEGER PRIMARY KEY, fruit VARCHAR(20), veges VARCHAR(30))')
con.commit()
cur.execute('INSERT INTO foo (o_id, fruit, veges) VALUES(NULL, "apple", "broccoli")')
con.commit()
    print (cur.lastrowid)

cur.execute('SELECT * FROM foo')
    print cur.fetchall()

