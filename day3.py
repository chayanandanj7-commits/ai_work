import sqlite3

conn = sqlite3.connect("applicants.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS applicants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    python_score INTEGER
)
""")

cursor.execute("""
INSERT INTO applicants (name, python_score)
VALUES ('Aman', 85), ('Priya', 95), ('Rahul', 70)
""")

conn.commit()

cursor.execute("SELECT * FROM applicants WHERE python_score < 80 ORDER BY python_score DESC")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()