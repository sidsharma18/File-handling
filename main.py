from pathlib import Path
import os

def readFileandFolder():
    path = Path(' ')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")



def createFile():
    try:
       readFileandFolder()
       name = input("Enter file name: ")
       p = Path(name)
       if not p.exists():
         with open(p,"w") as fs:
           data = input("what you want to write in inside: ")
           fs.write(data)

         print(F"FILE CREATED SUCCESSFULLY")
       else:
           print("this file already exists")

    except Exception as err:
        print(f"An error occurred: {err}")

def readFile():
    try:
      readFileandFolder()
      name = input("Which file you want to read: ")
      p = Path(name)
      if p.exists() and p.is_file():
          with open(p,"r") as fs:
              data = fs.read()
              print(data)
          print(F"FILE READ SUCCESSFULLY")
      else:
          print("this file does not exist")

    except Exception as err:
        print(f"An error occurred: {err}")

def  updateFile():
    try:
        readFileandFolder()
        name = input("Which file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for Changing the name of file: ")
            print("Press 2 for overwrite the data of file: ")
            print("Press 3 for append some content in your file: ")

            res = int(input("Enter your response: "))

            if res == 1:
                name2 = input("Tell your new file name")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p,'w') as fs:
                    data = input("tell what you want to write this will overwrite your data: ")
                    fs.write(data)

            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append: ")
                    fs.write(" "+data)

    except Exception as err:
        print(f"An error occurred: {err}")


def deleteFile():
    try:
      readFileandFolder()
      name = input("Which file you want to delete: ")
      p = Path(name)
      if p.exists() and p.is_file():
             os.remove(name)

             print("File Remove successful")

      else:
          print("this file does not exist")
    except Exception as err:
        print(f"An error occurred: {err}")



print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for Updating a file")
print("Press 4 for Deleting a file")

check = int(input("Enter your choice: "))
if check == 1:
    createFile()
if check == 2:
    readFile()
if check == 3:
    updateFile()
if check == 4:
    deleteFile()