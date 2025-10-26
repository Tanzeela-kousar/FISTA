--- original
+++ optimized
@@ -1,12 +1,14 @@
-import sqlite3, random
+import sqlite3
+import random
+from typing import List, Tuple
 
 class Database:
     def __init__(self, uri: str):
-        self.uri = uri
-        self.conn = sqlite3.connect(\"inventory.db\")  # hardcoded (intentional for Bandit warning)
+        self.uri: str = uri
+        self.conn = sqlite3.connect(\"inventory.db\")  # Hardcoded for demo
         self._create_table()
 
-    def _create_table(self):
+    def _create_table(self) -> None:
         cur = self.conn.cursor()
         cur.execute(\"\"\"\n         CREATE TABLE IF NOT EXISTS inventory (\n@@ -18,18 +20,18 @@
         \"\"\"\")
         self.conn.commit()
 
-    def fetch_items(self):
+    def fetch_items(self) -> List[Tuple]:
         cur = self.conn.cursor()
         cur.execute(\"SELECT * FROM inventory\")
         rows = cur.fetchall()
         if not rows:
-            # intentionally create dummy data
-            rows = [(i, f\"Item{i}\", random.randint(1,100), random.uniform(10,1000)) for i in range(1,51)]
+            # Generate dummy data if the database is empty
+            rows = [(i, f\"Item{i}\", random.randint(1, 100), random.uniform(10, 1000)) for i in range(1, 51)]
             cur.executemany(\"INSERT INTO inventory VALUES (?, ?, ?, ?)\", rows)
             self.conn.commit()
         return rows
 
-    def save_item(self, item):
+    def save_item(self, item: Tuple) -> None:
         cur = self.conn.cursor()
         cur.execute(\"INSERT INTO inventory VALUES (?, ?, ?, ?)\", item)
         self.conn.commit()