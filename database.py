import sqlite3

def init_db():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flavors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL,
                        season TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL,
                        quantity INTEGER NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        flavor_suggestion TEXT NOT NULL,
                        allergy_concern TEXT
                    )''')
    conn.commit()
    conn.close()

def add_flavor(name, season):
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO flavors (name, season) VALUES (?, ?)", (name, season))
    conn.commit()
    conn.close()

def add_ingredient(name, quantity):
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()

def add_customer_suggestion(flavor_suggestion, allergy_concern):
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customer_suggestions (flavor_suggestion, allergy_concern) VALUES (?, ?)", 
                   (flavor_suggestion, allergy_concern))
    conn.commit()
    conn.close()

def get_all_flavors():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, season FROM flavors")
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def get_all_ingredients():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity FROM ingredients")
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients
def get_all_suggestions():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute("SELECT flavor_suggestion, allergy_concern FROM customer_suggestions")
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions
