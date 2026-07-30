# folder management project ,
#creating a folder ,rename,delete,exit
import os
import sys
folder_name=""
print("=" *40)
print("File management system you can create ,delete,and renamea folder" )
print("=" *40)
print("\n""select your option" \
"\n1.create ," \
"\n2.delete, " \
"\n3.rename" 
"\n press any key to exit... "
"\n")

option=int(input("enter your option : 1,2 or 3\n "))

# Create Folder:
if (option == 1):

    folder_name=input("Enter Folder Name:  ")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("Folder is created successfully")
    else:
        print("folder already exists")
# Delete Folder
elif(option == 2):

    folder_name=input("Enter Folder Name:  ")
    if os.path.exists(folder_name):
         os.rmdir(folder_name)
         print("Folder is deleted successfully")
    else:
            print("folder not found")
elif(option == 3):
      
      folder_name=input("Enter existing Folder Name :  ")
      folder_new=input("Enter new Folder Name :  ")
      if os.path.exists(folder_name):
           os.rename(folder_name,folder_new)
           print("folder is renamed with new name ")
      else:
           print("old folder is not exist ")
else:
     sys.exit
    
     


