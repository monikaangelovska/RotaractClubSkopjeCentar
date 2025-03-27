## INSERT IMAGES FOR MEMBERS
import psycopg2
import os

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="Rotaract",
    user="postgres",
    password="monika2024"
)

if conn is not None:
    print("Connected to the PostgreSQL database.")

    cursor = conn.cursor()

    # Directory containing the images
    image_dir = r'C:\Users\User\Desktop\rotaract\members_images\add'

    # Map filenames to MemberID (example)
    filename_to_memberid = {
        # "neno.png": 6,
        # "leon.jpeg": 14,
        # "david.jpeg": 7,
        # "asib.jpg": 5
        # "iva.png": 13,
        # 'aleksandra.jpg': 3,
        # 'anja.jpg': 4,
        # 'bozin.jpg': 15,
        # 'darko jovanov.jpg': 11,
        # 'filip markoski.jpg': 16,
        # 'lidija.jpg': 10,
        # 'monika.jpg': 1,
        # 'petar andonoski.jpg': 8,
        # 'stefan.jpg': 2
        # Add more mappings as needed
    }

    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.JPG') or filename.endswith('.jpeg'):
            image_path = os.path.join(image_dir, filename)
            try:
                # Get the MemberID based on the filename
                member_id = filename_to_memberid.get(filename.lower())  # Use .lower() for case-insensitivity

                if member_id is None:
                    print(f"Error: No MemberID mapping found for {filename}")
                    continue  # Skip this file if no mapping exists

                # Read the image file as binary
                with open(image_path, 'rb') as file:
                    image_data = file.read()

                # Insert the image into the table
                cursor.execute(
                    """
                    INSERT INTO public."MembersImages" ("Image", "MemberID") 
                    VALUES (%s, %s)
                    """,
                    (psycopg2.Binary(image_data), member_id)  # Replace `None` with a valid MemberID if needed
                )
                conn.commit()
                print(f"Successfully inserted {filename}.")
            except (Exception, psycopg2.Error) as e:
                print(f"Error processing file {filename}: {e}")
                conn.rollback()  # Rollback the transaction on error

    # Close the connection
    conn.close()
    print("Connection closed.")
else:
    print("Failed to connect to the PostgreSQL database.")
