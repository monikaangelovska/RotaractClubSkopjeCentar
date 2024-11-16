import os

def print_folders_recursively(folder_path):
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isdir(full_path):
            print(full_path)  # Print the folder name
            # Recursively call the function to print subfolders
            print_folders_recursively(full_path)

# Specify the root folder path
folder_path = r'C:\Users\User\Desktop\Diplomska proekt\RotaractProject'
print_folders_recursively(folder_path)
