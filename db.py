import sqlite3
import pandas as pd

# Load the CSV file
csv_file = 'questions.csv'
data = pd.read_csv(csv_file)

# Create SQLite database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    question TEXT
)
''')

# Insert data into the table
data.to_sql('questions', conn, if_exists='replace', index=False)

conn.close()
print("Database created and data inserted.")
