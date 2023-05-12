# File Deletion Script with GUI
This Python script deletes files in a selected directory that contain a specified string in their filename. It features a simple graphical user interface (GUI) for user input and supports filtering by file type.

# Requirements
Python 3.6 or higher

# Usage
Run the script:
python delete_files.py
When prompted, select a directory in the file explorer window.

Enter a string to filter filenames. The script will delete all files in the selected directory that contain this string in their filename.

When prompted, choose whether to delete all file types or only specific ones. If you choose specific ones, you'll be prompted to enter the extensions of the file types you want to delete.

The script will then delete the matching files and display a message box saying "Files deleted successfully!".

After the files are deleted, a window with an "Exit" button will appear. Click this button to close the application.

# Customization
The window icon can be customized by replacing 'your_icon.ico' in the script with the path to your icon file. The icon file needs to be in .ico format.
# Warning
This script will permanently delete files. Always make sure to back up your files before running a file deletion script.
