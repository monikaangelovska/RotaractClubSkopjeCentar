## INSERT IMAGES FOR PROJECT
import psycopg2
import os

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="db",
    database="rotaract",
    user="postgres",
    password="monika2024"
)
# conn = psycopg2.connect(
#     host="localhost",
#     database="Rotaract",
#     user="postgres",
#     password="monika2024"
# )

if conn is not None:
    print("Connected to the PostgreSQL database.")

    cursor = conn.cursor()

    # Directory containing the images
    # image_dir = '/rotaract_website/sliki'
    image_dir = r'C:\Users\User\Desktop\Diplomska proekt\RotaractProject\sliki'

    for image_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_name)

        # Skip if it's not a file
        if not os.path.isfile(image_path):
            continue

        try:
            # Extract the date (first 10 characters) and project ID (characters between "_" and "(")
            image_date = image_name[:10]  # First 10 characters
            project_id = image_name.split('_')[1].split('(')[0]  # Between "_" and "("

            # Read the image data
            with open(image_path, 'rb') as file:
                image_data = file.read()

            # Insert into the Images table
            insert_query = """
                INSERT INTO public."Images" (image_data, image_date, project_id)
                VALUES (%s, %s, %s);
            """
            cursor.execute(insert_query, (image_data, image_date, project_id))
            conn.commit()
            print(f"Inserted: {image_name}")
        except Exception as e:
            conn.rollback()
            print(f"Failed to insert {image_name}: {e}")

    # Close the cursor and connection
    cursor.close()
    conn.close()
    print("Database connection closed.")
else:
    print("Failed to connect to the PostgreSQL database.")
