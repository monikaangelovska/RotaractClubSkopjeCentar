# # INSERT NEW PROJECT
# import psycopg2

# # Connect to PostgreSQL database
# conn = psycopg2.connect(
#     host="db",
#     database="rotaract",
#     user="postgres",
#     password="monika2024"
# )

# if conn is not None:
#     print("Connected to the PostgreSQL database.")

#     cursor = conn.cursor()
#     name = "Men's Health Matters"
#     description = "In November 2024, to mark Men's Health Month, our club organized an internal lecture titled \"Men's Health Matters,\" presented by Dr. Spec. Elena Kitevska from the University Clinic of Urology. Dr. Kitevska shared her expertise on preventive healthcare, the importance of regular medical check-ups, and ways to maintain men's health. Through this, the club aims to raise awareness about health care for men and encourage greater engagement in preventive measures to preserve health."
#     start_date = "2024-11-28"
#     end_date = start_date

#     try:
#         # Exclude the "id" column, letting PostgreSQL auto-generate it
#         insert_query = """
#                 INSERT INTO public."EventProject" (id, name, description, start_date, end_date)
#                 VALUES (42, %s, %s, %s, %s);
#             """
#         cursor.execute(insert_query, (name, description, start_date, end_date))
#         conn.commit()
#         print("Data inserted successfully!")
#     except Exception as e:
#         conn.rollback()
#         print(f"An error occurred: {e}")

#     # Close the cursor and connection
#     cursor.close()
#     conn.close()
#     print("Database connection closed.")
# else:
#     print("Failed to connect to the PostgreSQL database.")






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

if conn is not None:
    print("Connected to the PostgreSQL database.")

    cursor = conn.cursor()

    # Directory containing the images
    image_dir = '/rotaract_website/sliki'

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





## INSERT IMAGES FOR MEMBERS
# import psycopg2
# import os

# # Connect to PostgreSQL database
# conn = psycopg2.connect(
#     host="db",
#     database="rotaract",
#     user="postgres",
#     password="monika2024"
# )

# if conn is not None:
#     print("Connected to the PostgreSQL database.")

#     cursor = conn.cursor()

#     # Directory containing the images
#     image_dir = '/rotaract_website/members_images'

#     # Map filenames to MemberID (example)
#     filename_to_memberid = {
#         # 'aleksandra.jpg': 3,
#         # 'anja.jpg': 4,
#         # 'bozin.jpg': 15,
#         # 'darko jovanov.jpg': 11,
#         # 'filip markoski.jpg': 16,
#         # 'lidija.jpg': 10,
#         # 'monika.jpg': 1,
#         # 'petar andonoski.jpg': 8,
#         # 'stefan.jpg': 2
#         # Add more mappings as needed
#     }

#     for filename in os.listdir(image_dir):
#         if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.JPG'):
#             image_path = os.path.join(image_dir, filename)
#             try:
#                 # Get the MemberID based on the filename
#                 member_id = filename_to_memberid.get(filename.lower())  # Use .lower() for case-insensitivity

#                 if member_id is None:
#                     print(f"Error: No MemberID mapping found for {filename}")
#                     continue  # Skip this file if no mapping exists

#                 # Read the image file as binary
#                 with open(image_path, 'rb') as file:
#                     image_data = file.read()

#                 # Insert the image into the table
#                 cursor.execute(
#                     """
#                     INSERT INTO public."MembersImages" ("Image", "MemberID") 
#                     VALUES (%s, %s)
#                     """,
#                     (psycopg2.Binary(image_data), member_id)  # Replace `None` with a valid MemberID if needed
#                 )
#                 conn.commit()
#                 print(f"Successfully inserted {filename}.")
#             except (Exception, psycopg2.Error) as e:
#                 print(f"Error processing file {filename}: {e}")
#                 conn.rollback()  # Rollback the transaction on error

#     # Close the connection
#     conn.close()
#     print("Connection closed.")
# else:
#     print("Failed to connect to the PostgreSQL database.")
