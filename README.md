#File Sorting Script
##Description
This Python script automatically organizes files in the Downloads folder into categorized subfolders based on their file types. It sorts images, videos, and documents into 'Images', 'Videos', and 'Documents' subfolders respectively, according to their file extensions.

##Features
Automatically detects and sorts files into designated subfolders.
Handles common file formats for images, videos, and documents.
Includes basic error handling for file operations.

##Requirements
Python 3.x
PyInstaller (for creating an executable file)

##Installation and Setup
Ensure Python 3.x is installed on your system.
Clone or download this repository to your local machine.
(Optional) If you want to create an executable:
Install PyInstaller using pip install pyinstaller.
Run pyinstaller --onefile sort.py in the command line within the project directory.
Usage
Run the script directly with Python:
lua
Copy code
python sort.py
Or, if you have created an executable, simply double-click on the executable file.

##How It Works
The script scans the Downloads folder for files and organizes them into 'Images', 'Videos', and 'Documents' based on the file extension. It creates these subfolders if they do not already exist. The script is equipped to handle errors like file access issues and will log any such occurrences.

##Supported File Extensions
Images: .jpg, .jpeg, .png, .svg
Videos: .mp4, .avi, .mov
Documents: .pdf, .docx, .txt
Executables: .exe

##Customization
You can modify the file_type dictionary in the script to add or change the file categories and their associated file extensions.
