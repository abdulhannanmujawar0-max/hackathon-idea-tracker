import sqlite3

# 1. Connect to the database (this creates the file if it doesn't exist)
connection = sqlite3.connect("ideas.db")

# 2. Create a cursor object to execute SQL commands
cursor = connection.cursor()

# 3. Write raw SQL to create a table with three columns: id, title, and status
cursor.execute("""
CREATE TABLE IF NOT EXISTS hackathon_ideas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'pending'
)
""")

# 4. Save the changes and close the connection
connection.commit()
connection.close()

print("Success! Database and table created.")