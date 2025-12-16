import sqlite3

from clinic import resource_path 

def create_db():
   con = sqlite3.connect(resource_path('clinic.db'))
   cur = con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS xrays(address text, contact text, price text, state text,date text, age text, gender text, name text, xid INTEGER PRIMARY KEY AUTOINCREMENT )")
   con.commit()
   
   cur.execute("CREATE TABLE IF NOT EXISTS dental(address text, contact text, state text,date text, age text, gender text, name text,aid INTEGER PRIMARY KEY AUTOINCREMENT )")
   con.commit()   
   
   cur.execute("CREATE TABLE IF NOT EXISTS implant(cont text, con2 text, con1 text, con text, price text, type text, address text, contact text, date text, age text, gender text, name text,pid INTEGER PRIMARY KEY AUTOINCREMENT )")
   con.commit()   
   
   cur.execute("CREATE TABLE IF NOT EXISTS press(cont text, con text, price text, type text, address text, contact text, date text, age text, gender text, name text,pid INTEGER PRIMARY KEY AUTOINCREMENT )")
   con.commit() 
   
   
   
create_db()   