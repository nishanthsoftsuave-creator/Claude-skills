import sqlite3

DB = "inventory.db"


def init():
    with sqlite3.connect(DB) as c:
        c.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, qty INTEGER)")


def add(name, qty):
    with sqlite3.connect(DB) as c:
        c.execute("INSERT INTO items (name, qty) VALUES (?, ?)", (name, qty))


def list_items():
    with sqlite3.connect(DB) as c:
        return c.execute("SELECT id, name, qty FROM items").fetchall()
