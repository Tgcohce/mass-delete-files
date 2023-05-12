

import os
import glob
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def delete_files():
    # Prompt the user for the directory
    dir_path = filedialog.askdirectory(title="Select Directory")

    # Prompt the user for the string to filter filenames
    filter_string = simpledialog.askstring("Input", "File names that contain this will be deleted:")

    # Prompt the user to choose whether to delete all file types or only specific ones
    all_file_types = messagebox.askyesno("Question", "Do you want to delete all types of files? (No if only specific types)")

    # If the user chose to delete only specific file types, prompt them to enter the extensions
    extensions = []
    if not all_file_types:
        extensions = simpledialog.askstring("Input", "Enter the file extensions to delete (comma separated: pdf,txt,xls):").split(',')

    if not dir_path or not filter_string:
        return

    if all_file_types:
        # Get a list of all files in the directory
        files = glob.glob(os.path.join(dir_path, '*'))
    else:
        # Get a list of files in the directory with the specified extensions
        files = []
        for ext in extensions:
            files += glob.glob(os.path.join(dir_path, f'*.{ext.strip()}'))

    # Loop through the files and delete those that contain the filter string in their name
    for file in files:
        if filter_string in os.path.basename(file):
            os.remove(file)
            print(f'Deleted file: {file}')

    messagebox.showinfo("Completed", "Files deleted successfully!")
    root.deiconify()  # Show the main window with the Exit button

root = tk.Tk()
root.withdraw()  # Hide the main window initially
root.iconbitmap('my_icon.xbm')  # Change the window icon
root.title("Delete Files")

exit_button = tk.Button(
    root,
    text="Exit",
    command=root.quit
)
exit_button.pack()  # Pack the exit button, but it won't be visible until the main window is shown

delete_files()

root.mainloop()
