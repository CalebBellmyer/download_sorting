"""
This script organizes files in the Downloads folder into subfolders based on their file types.
It sorts images, videos, and documents into 'Images', 'Videos', and 'Documents' subfolders 
respectively, according to their file extensions. The script handles common file formats for 
each category and includes basic error handling for file operations.
"""
import os
import shutil


file_type = {
    'Images': ['.jpg', '.jpeg', '.png', '.svg'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Documents': ['.pdf','.docx', '.txt'],
    'Executables': ['.exe']
}

# Path to download folder
DOWNLOAD_PATH = os.path.join(os.environ['USERPROFILE'], 'Downloads')

# Create subfolders
for folder in file_type:
    os.makedirs(os.path.join(DOWNLOAD_PATH, folder), exist_ok=True)


# look through downloads folders
for file in os.listdir(DOWNLOAD_PATH):
    file_path = os.path.join(DOWNLOAD_PATH, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        for folder, extensions in file_type.items():
            if ext in extensions:
                try:
                    shutil.move(file_path, os.path.join(DOWNLOAD_PATH, folder, file))
                except Exception as e:
                    print(f"Error moving file {file}: {e}")
                break

print("Files sorted successfully")
