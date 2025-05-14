If your script has been compiled into an executable (EXE), here's an updated version of the README that includes instructions for running the executable:

---

# File Sorting and Backup Script

This Python script helps you organize and back up your files by sorting them based on their **creation** or **modification** dates and allowing for a backup of files to a specified location. The script can be run either as a **Python script** or as a compiled **EXE** file.

## Features

1. **Sort Files by Date**

   * The script can organize files in a folder into subfolders based on either **creation dates** or **modification dates**.
   * After sorting, the files will be moved into subfolders named by the year and month of their respective creation or modification date.

2. **Backup Files**

   * The script can also create a backup of the files in a specified folder and save them to a target location.
   * It will delete any existing backup folder before creating a new one, ensuring only the latest backup is available.

## Prerequisites

### For Python Script:

* Python 3.x
* `shutil` (Standard Library)
* `os` (Standard Library)
* `time` (Standard Library)
* `datetime` (Standard Library)

### For EXE:

* No installation of Python required. Simply run the **EXE** file.

## How to Use

### Running the Python Script

1. **Clone or Download the Script**:

   * Download the Python script to your local machine.

2. **Execute the Script**:

   * Run the script from a terminal or command prompt:

   ```bash
   python file_sorter_backup.py
   ```

3. **Options**:

   * The script will prompt you to choose between **sorting** files or **backing up** files.

     * **Sort**: Organizes the files in a folder based on either their **Creation Dates (Ct)** or **Modification Dates (Mt)**.
     * **Backup**: Copies all files from a selected folder to a backup directory.

### Running the EXE

1. **Download the EXE**:

   * Download the compiled **EXE** file.

2. **Run the EXE**:

   * Double-click the **EXE** file to launch the program. You can run it directly without needing Python installed.

3. **Options**:

   * Once the program launches, it will prompt you to choose between sorting files or backing them up.
   * **Sort**: Similar to the Python script, it will ask you to select the folder and sorting criteria (Creation Date or Modification Date).
   * **Backup**: It will prompt you to select the source folder to back up and the destination for the backup.

### Sorting Files

1. Enter the path of the folder you want to sort.
2. Choose whether to sort the files by **Creation Date (Ct)** or **Modification Date (Mt)**.
3. The script will create new subfolders named by the year and month (`YYYY-MM`) and move the files accordingly.
4. You can type `'quit'` to exit the program at any time.

### Backing Up Files

1. Enter the folder path you want to back up.
2. Enter the destination where the backup will be stored.
3. The script will delete any existing backup folder at the destination and create a new backup folder named "Backup".

### Example Usage

1. **Sort Files**:

   ```plaintext
   Do you want to sort or backup(sort, backup): sort
   What Folder do you Want to sort: C:\Users\Username\Documents
   Would you like to sort by Creation Dates Or Modification Dates (Ct,Mt): ct
   ```

2. **Backup Files**:

   ```plaintext
   Do you want to sort or backup(sort, backup): backup
   Which folder do you want to backup: C:\Users\Username\Documents
   Where do you want to backup: D:\BackupFolder
   ```

## Handling Errors

* If the folder path does not exist, the script will inform you and prompt for a valid path.
* If the file cannot be moved or copied due to permission errors, the script will print an error message and continue with the next file.

## Requirements (For Python Script)

* Ensure the `os`, `shutil`, `datetime`, and `time` libraries are available (they come with Python by default).

---

This version of the README includes instructions for both the Python script and the EXE version. Let me know if you'd like to further refine it!
