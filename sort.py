import os
from datetime import datetime as dt
import shutil as sh
import time
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
global_read_flies = []
name = ""

def seeflies(folder):
 
   global real_date_obj
   global global_read_flies

   print("📁 The files in your path are being read...")
   time.sleep(2)

   global_read_flies = os.listdir(folder)
   sort = input("Would you like to sort by Creation Dates Or Modification Dates(Ct,Mt)?: ").lower()
   if sort == "ct":


     print(f"The files in your path are: {global_read_flies}")
     print("Getting Creation Dates...")
     time.sleep(2)


     for file in global_read_flies:
        global name_file
        filepath = os.path.join(folder, file)

        
        
   

        ctime = os.path.getctime(filepath)
        date_obj = dt.fromtimestamp(ctime).strftime('%Y-%m-%d')
        real_date_obj = dt.fromtimestamp(ctime).strftime('%Y-%m')        
        print(f"Creation date:{file} ➡ {date_obj}")
        

        name_file = f"{real_date_obj}"
        os.makedirs(name_file, exist_ok=True)
        if os.path.isdir(os.path.join(filepath, name_file)):
           print(f"Skipping This director: {file}")
           continue   
     
        try:
          sh.move(filepath, os.path.join(name_file, file))
        except (sh.Error, FileNotFoundError, PermissionError) as e:
          print(f"❌ Could not move {file}: {e}")
          continue
        
        

           
        

   if sort == "mt":
      print(f"The files in your path are: {global_read_flies}")
      print("Getting Modification Dates...")
      time.sleep(2)

      for file in global_read_flies:
        filepath = os.path.join(folder, file)


   

        mtime = os.path.getmtime(filepath)
        date_obj = dt.fromtimestamp(mtime).strftime('%Y-%m-%d')
        real_date_obj = dt.fromtimestamp(mtime).strftime('%Y-%m')        
        print(f"Modification date:{file} ➡ {date_obj}")
        
        
        
        
        name_file = f"{real_date_obj}"
        os.makedirs(name_file, exist_ok=True)
        if os.path.isdir(os.path.join(filepath, name_file)):
           print(f"Skipping This director: {file}")
           continue   
      


        try:
          sh.move(filepath, os.path.join(name_file, file))
        except (sh.Error, FileNotFoundError, PermissionError) as e:
          print(f"❌ Could not move {file}: {e}")
          continue

           
        

def backup(folder,destination):
   
   print("📁 Please Delete previous backup file, if you are backing up again")
   print("📁 The files in your path are being read...")
   time.sleep(2)
   list_of_folder_to_backup = os.listdir(folder)
   see_list = input("Do you wan to see the files in the directory?(Yes,No)").lower()
   if see_list == "yes":
      print(f"The files and folders in the directory are:\n{list_of_folder_to_backup}")
   elif see_list == "no": 
      pass
   else:
      print("Invalid Input!")
    
   os.chdir(destination)
   backup_path = os.path.join(destination, "Backup")
   if os.path.exists(backup_path):
      sh.rmtree(backup_path)
   os.makedirs("Backup", exist_ok= True)
   for file in list_of_folder_to_backup:
      filepath = os.path.join(folder, file)
      target_path = os.path.join(backup_path, file)
      try:
        sh.copy2(filepath, target_path)
      except (sh.Error, FileNotFoundError, PermissionError) as e:
          print(f"❌ Could not copy {file}: {e}")
          continue
    
      
      
      
   
   
   
   
while True:
  

   
  cwd = os.chdir(desktop_path)
  print(F"📍 Current Working Directory: {os.getcwd()}")
  backup_sort = input("Do you want to sort or backup(sort,backup)").lower()
  if backup_sort == "sort":
    print("Type \'quit\' to exit the program in lowrcase")
    folder_to_sort = input("📁 What Folder do you Want to sort(give path without colons):").strip()
  

    if os.path.exists(folder_to_sort):
      os.chdir(folder_to_sort)
      time.sleep(2)
      print(F"📍 Current Working Directory: {os.getcwd()}")
      seeflies(folder_to_sort)
      print("Files in the folder have been organised 😁!")
      
      

    elif folder_to_sort == "quit":
     break

    else:
     print("❌ Directory does not exist. Please check your path.")
    

  if backup_sort == "backup":
    print("Type \'quit\' to exit the program in lowrcase")
    folder_to_backup = input("Which folder do you want to backup?(give path without colons): ") 
    destination = input("Where do you want to backup?(give path without colons): ") 
    backup(folder_to_backup,destination)
     
