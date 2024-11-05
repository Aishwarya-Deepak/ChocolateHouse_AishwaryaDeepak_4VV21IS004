import sqlite3
def init_db():
    conn=sqlite3.connect("chocolate.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flavours(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL, season TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL, quantity INTEGER NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS suggestions(id INTEGER PRIMARY KEY AUTOINCREMENT, suggestion TEXT NOT NULL, allergy TEXT)''')
    conn.commit()
    conn.close()
def yourflavour(name,season):
    conn=sqlite3.connect("chocolate.db")
    cursor=conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO flavours (name,season) VALUES (?,?)",(name,season))
    conn.commit()
    conn.close()
def youringredient(name,quantity):
    conn=sqlite3.connect("chocolate.db")
    cursor=conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO ingredients (name,quantity) VALUES (?,?)",(name,quantity))
    conn.commit()
    conn.close()
def yoursuggestion(suggestion,allergy):
    conn=sqlite3.connect("chocolate.db")
    cursor=conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO suggestions (suggestion,allergy) VALUES (?,?)",(suggestion,allergy))
    conn.commit()
    conn.close()
def displayflavours():
    conn=sqlite3.connect("chocolate.db")
    cursor=conn.cursor()
    cursor.execute("SELECT name,season FROM flavours")
    flavours=cursor.fetchall()
    conn.close()
    return flavours
def displayingredients():
    conn=sqlite3.connect("chocolate.db")
    cursor=conn.cursor()
    cursor.execute("SELECT name,quantity FROM ingredients")
    ingredients=cursor.fetchall()
    conn.close()
    return ingredients
def displaysuggestions():
    conn=sqlite3.connect("chocolate.db")
    cursor=conn.cursor()
    cursor.execute("SELECT suggestion,allergy FROM suggestions")
    suggestions=cursor.fetchall()
    conn.close()
    return suggestions