import os

oldname="boo"
newname="mini_project"

if os.path.exists(oldname):
    os.rename(oldname,newname)
    print("successfully renamed")
else:
    print("folder is not founded")
    
