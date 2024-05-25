import sqlite3

connect=sqlite3.connect("database.db")
cursor=connect.cursor()
class Database:
    def __init__(self):
        print("database")
        self.connect=sqlite3.connect("database.db")
        self.cursor=self.connect.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
        name Text NOT NULL,
        phone Text NOT NULL
        )""")
        self.connect.commit()
    def save(self):
        print(self.name)
        print(self.telefon)
        self.cursor.execute(""" INSERT INTO users(name,telefon) VALUES(?,?)""",
                            (self.name, self.telefon))
        self.connect.commit()
    def all(self):
        self.cursor.execute("SELECT * FROM users")
        return  self



