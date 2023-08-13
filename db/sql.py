import sqlite3

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.balance = 0.00
        self.transactions = 0

    # add new user
    def save(self):
        conn = sqlite3.connect("./db/db.sqlite", check_same_thread=False)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, balance FLOAT, transactions INTEGER)")

        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (self.username, self.password, self.balance, self.transactions))
        conn.commit()

    # check if nuname taken or short
    def is_username_valid(self):
        conn = sqlite3.connect("./db/db.sqlite", check_same_thread=False)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, balance FLOAT, transactions INTEGER)")

        if len(self.username) < 4:
            return False
        users = c.execute("SELECT * FROM users").fetchall()
        for user in users:
            if self.username in user[0]:
                return False
        return True

    # check if pw is short
    def is_password_valid(self):
        if len(self.password) >= 8:
            return True
        else:
            return False
    
    # try to login
    def login(self):
        conn = sqlite3.connect("./db/db.sqlite", check_same_thread=False)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, balance FLOAT, transactions INTEGER)")
        
        users = c.execute("SELECT * FROM users").fetchall()
        for user in users:
            if self.username in user[0] and self.password in user[1]:
                return True
        return False

class Post:
    def __init__(self, username, transaction_date, merchant, amount) -> None:
        self.username = username
        self.transaction_date = transaction_date
        self.merchant = merchant

    def save(self):
