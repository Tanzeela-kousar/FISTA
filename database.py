import sqlite3, random

class Database:
    def __init__(self, uri: str):
        self.uri = uri
        self.conn = sqlite3.connect("inventory.db")  # hardcoded (intentional for Bandit warning)
        self._create_table()

    def _create_table(self):
        cur = self.conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER,
            price REAL
        )
        """)
        self.conn.commit()

    def fetch_items(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM inventory")
        rows = cur.fetchall()
        if not rows:
            # intentionally create dummy data
            rows = [(i, f"Item{i}", random.randint(1,100), random.uniform(10,1000)) for i in range(1,51)]
            cur.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?)", rows)
            self.conn.commit()
        return rows

    def save_item(self, item):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO inventory VALUES (?, ?, ?, ?)", item)
        self.conn.commit()
