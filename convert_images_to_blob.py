import sqlite3
import os
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect(r'C:\Users\User\Desktop\Diplomska proekt\RotaractProject\db.sqlite3')

if conn is not None:
    print("Connected to the SQLite database.")

    cursor = conn.cursor()

    image_dir = r'C:\Users\User\Desktop\rotaract\rotaract old\stari sliki'

    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            try:
                date_part, project_id_part = filename.split('_', 1)

                date_str = date_part.split('(')[0]

                date = datetime.strptime(date_str, '%Y-%m-%d').date()

                project_id = int(project_id_part.split('.')[0]) 

                with open(os.path.join(image_dir, filename), 'rb') as f:
                    image_data = f.read()

                cursor.execute("INSERT INTO images_test (image_data, image_date, project_id) VALUES (?, ?, ?)", 
                               (image_data, date, project_id))
                conn.commit()
                
            except (ValueError, IndexError) as e:
                print(f"Error processing file {filename}: {e}")

    conn.close()
else:
    print("Failed to connect to the SQLite database.")
