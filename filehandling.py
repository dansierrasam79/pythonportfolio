# create file
def createfiles(dirpath,filesList):
    for fileName in filesList:
        filepath = dirpath+fileName
        newEmptyFile = open(filepath, "w") # old way of creating a file
        newEmptyFile.write("This is the first line of the new file.")
        newEmptyFile.write("\n")
        newEmptyFile.close()
# rename file
def renamefiles(dirpath,filesList,newfilesList):
    for idx in range(0, len(filesList)):
        oldfilename = dirpath+filesList[idx]
        newfilename = dirpath+newfilesList[idx]
        os.rename(oldfilename,newfilename)

# append file
def appendtofile(dirpath,filename):
    filepath = dirpath+filename
    if filename in os.listdir(dirpath):
        fName = open(filepath, "a")
        fName.write("\n")
        fName.write("First append")
        fName.write("\n")
        fName.write("Second append")
        fName.close()

# read file
def readfile(dirpath,filename):
    filepath = dirpath+filename
    if filename in os.listdir(dirpath):
        fName = open(filepath, "r")
        fullText = fName.read()
        fName.close()
        print(fullText)
    else:
        print(filename, "does not exist!")

# delete file
def deletefiles(dirpath,filesList):
    for fileName in filesList:
        filepath = dirpath+fileName
        if fileName in os.listdir(dirpath):
            os.remove(filepath)
        else:
            print(filepath, "does not exist.")

def movefiles(dirpath,dirpath2,filesList):
    for fileName in filesList:
        oldfilepath = dirpath+fileName
        newfilepath = dirpath2+fileName
        os.rename(oldfilepath,newfilepath)

def quality_check_add(dirpath,filesList):
    for fileName in filesList: 
        if fileName in os.listdir(dirpath): 
            print("Success. File Created.") 
        else: 
            print("Error. File NOT Created.")

def quality_check_delete(dirpath,filesList):
    for fileName in filesList: 
        if fileName in os.listdir(dirpath): 
            print("Error. File NOT deleted.")
        else: 
            print("Success. File deleted.")

def quality_check_rename(dirpath,newfilesList):
    for fileName in newfilesList:
        if fileName in os.listdir(dirpath):
            print("File name changed.")
        else:
            print("Error. No such file name.")

def quality_check_move(dirpath2,filesList):
    for fileName in filesList:
        if fileName in os.listdir(dirpath2):
            print("Directory changed.")
        else:
            print("Error. No such file name.")

if __name__ == "__main__":
    import os,sys
    # add filenames to filesList with suitable extension for all operations
    filesList = ["test1.txt", "test1.xlsx", "test1.docx","test1.py"]
    # add old files names in filesList and new file names in newfilesList to rename files
    newfilesList = ["test2.txt", "test2.xlsx", "test2.docx","test2.py"]
    # please enter the directory to carry out file operations
    dirpath = r"C:\\Users\\danielchakraborty\\Desktop\\test\\"
    # please enter destination directory for moving files
    dirpath2 = r"C:\\Users\\danielchakraborty\\Desktop\\test2\\"
    while True:
        print("***Menu***")
        print("1. Create files")
        print("2. Delete files")
        print("3. Rename files")
        print("4. Move files")
        print("5. Read file contents")
        print("6. Append file contents")
        print("7. Exit")
        useri = int(input("Please select an option (1-7): "))
        match useri:
            case 1:
                createfiles(dirpath,filesList)
                quality_check_add(dirpath,filesList)
            case 2:
                deletefiles(dirpath,filesList)
                quality_check_delete(dirpath,filesList)
            case 3:
                renamefiles(dirpath,filesList,newfilesList)
                quality_check_rename(dirpath,newfilesList)
            case 4:
                movefiles(dirpath,dirpath2,filesList)
                quality_check_move(dirpath2,filesList)
            case 5:
                filename = input("Enter file name: ")
                readfile(dirpath,filename)
            case 6:
                filename = input("Enter file name: ")
                appendtofile(dirpath,filename)
            case 7:
                print("Thank you for using this file handling system")
                sys.exit()
            case _:
                print("Incorrect selection.")
                usr = input("Do you want to continue (Y/N)?: ").lower()
                match usr:
                    case "y":
                        continue;
                    case "n":
                        print("Thank you for using this file handling system")
                        sys.exit()
