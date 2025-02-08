import psycopg2

conn = psycopg2.connect(
    host="db",
    database="rotaract",
    user="postgres",
    password="monika2024"
)

cursor = conn.cursor()

# Select rows from UpcomingEvents where date < current date
cursor.execute("""SELECT * 
                  FROM public."UpcomingEvents" 
                  WHERE date < CURRENT_DATE;""")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Insert rows into EventProject table
for row in rows:
    event_name = row[1]       
    description = row[2]     
    start_date = row[3]     
    end_date = row[3]         

    cursor.execute("""INSERT INTO public."EventProject" ("name", "description", "start_date", "end_date") 
                      VALUES (%s, %s, %s, %s);""", 
                   (event_name, description, start_date, end_date))

conn.commit()

# Delete the rows from UpcomingEvents where date < current date
cursor.execute("""DELETE FROM public."UpcomingEvents" 
                  WHERE date < CURRENT_DATE;""")

conn.commit()

print(f"Successfully inserted {len(rows)} rows into the EventProject table and deleted them from UpcomingEvents.")

cursor.close()
conn.close()