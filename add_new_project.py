# # INSERT NEW PROJECT
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="db",
    database="rotaract",
    user="postgres",
    password="monika2024"
)

if conn is not None:
    print("Connected to the PostgreSQL database.")

    cursor = conn.cursor()
    name = ""
    description = ""
    start_date = ""
    end_date = start_date

    try:
        # Exclude the "id" column, letting PostgreSQL auto-generate it
        insert_query = """
                INSERT INTO public."EventProject" (id, name, description, start_date, end_date)
                VALUES ([vnesi id racno], %s, %s, %s, %s);
            """
        cursor.execute(insert_query, (name, description, start_date, end_date))
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {e}")

    # Close the cursor and connection
    cursor.close()
    conn.close()
    print("Database connection closed.")
else:
    print("Failed to connect to the PostgreSQL database.")
