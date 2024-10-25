import os
import re

# Directory containing images
image_dir = r'C:\Users\User\Desktop\rotaract\rotaract old\stari sliki'

pattern = r"_(\d+)\."

# Extract the numbers and sort them
extracted_numbers = []
for filename in os.listdir(image_dir):
    print(f"Checking filename: {filename}")
    match = re.search(pattern, filename)
    if match:
        extracted_numbers.append(int(match.group(1)))  # Convert to int for sorting

# Sort the extracted numbers
sorted_numbers = sorted(extracted_numbers)
print("Sorted extracted numbers:", sorted_numbers)
