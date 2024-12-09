import sqlite3

# Connect to SQLite database
conn = sqlite3.connect(r'C:\Users\User\Desktop\Diplomska proekt\db.sqlite3')

cursor = conn.cursor()

# Corrected query for SQLite
cursor.execute("""SELECT * 
                  FROM "UpcomingEvents" 
                  WHERE date < datetime('now');""")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Print the rows
for row in rows:
    event_name = row[1]
    description = row[2]
    start_date = row[3]
    end_date = row[3]

    cursor.execute("""INSERT INTO "EventProject" ("name", "description", "start_date", "end_date") 
                      VALUES (?, ?, ?, ?);
                   """, (event_name, description, start_date, end_date))

# commit the insertion
conn.commit()

# Delete the rows from UpcomingEvents where date < datetime('now')
cursor.execute("""
DELETE FROM "UpcomingEvents" 
WHERE date < datetime('now');
""")

# Commit the deletion
conn.commit()

# Print success message
print(f"Successfully inserted {len(rows)} rows into the EventProject table and deleted them from UpcomingEvents.")

# Close the cursor and connection
cursor.close()
conn.close()
