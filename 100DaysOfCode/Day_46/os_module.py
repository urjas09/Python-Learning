import os

if not os.path.exists("data"):
 os.mkdir("data") #this cmd makes a data directory inside this folder

#now supoose you want to make a folder for 100 days inside data 
#for i in range(0,100):
 #   os.mkdir(f"data/Day_{i+1}") 
#this line of the code gives an error since we have already created data file above.The solution for this is to give a condition that If a folder named 'data' does not already exist in the current working directory, create it.
#Breaking it down line by line:
# Line 3 (if not os.path.exists("data"):): Checks if a file or folder named "data" is missing.
# Line 4 (os.mkdir("data")): Creates the "data" folder only if the check in line 3 was true.
# This check prevents your Python script from crashing with a FileExistsError if you run the program more than once.
#If you are running all the code at once it will not give an error.
#This command makes it time efficient and easier to create 100 days folders all at once just by running a command.

#rename folders using os module
for i in range(0,100):
  os.rename(f"data/Day_{i+1}", f"data/Tut_{i+1}") # f"data/Day_{i+1}"->source & f"data/Tut_{i+1}"->destination(the name with which you want to rename the folder)

folders = os.listdir("data")    #tells the list of folders present in data directory
print(folders) 

#If you want data of the folders inside these folders
for folder in folders:
  print(folder)
  print(os.listdir(f"data/{folder}")) #this shows all the tut foders empty except tut_1 since it contains a md fie.
#This can be used for creating your own user-defined search searching files in folders in OS at the place of the built-in search sustems of the OS.

#os.system() - This method in Python is part of the built-in os module and is used to execute a system command string directly in the operating system's subshell.
#Eg. using os.system to get current date of the system
cmd = 'date /t' #/t stops windows from asking 'enter new date' after printing the date in the console
os.system(cmd)

#NOTE - 
#The strikethrough line means that os.system() has been officially soft-deprecated in Python.
#Your program still runs perfectly fine because a "soft deprecation" means the feature will not be removed or broken immediately so that older code keeps working. Instead, it serves as a visual warning from your code editor (like VS Code's Pylance extension) informing you that a safer, better tool now exists.

#Why is it discouraged?

# Security Risks: It leaves code highly vulnerable to shell execution exploits.
# Limited Control: It does not let you capture data or error outputs back into Python variables easily.

#The Modern Solution

#To get rid of the strikethrough warning and use up-to-date Python standards, replace os.system() with the subprocess module:
import subprocess

cmd2 = 'date /t'
subprocess.run(cmd, shell=True)

#os.getcwd() method tells at which directory you are currently. 
print(os.getcwd())   #output -C:\Users\ACER\Desktop\Python-Learning
#one can change the current working directory using os.chdir()
#os.chdir() is a built-in Python method from the os module used to change the current working directory of the running process to a specified destination folder & "of the running process to a specified destination folder" means your running script switches its current focus to a new target folder so that any files it opens or saves next will be looked for or placed inside that specific folder.

#os.chdir("/Users")  
#print(os.getcwd())
#for folder in folders:
 # print(folder)
 # print(os.listdir(f"data/{folder}"))
#If the this for loop is  run after this os.chdir() , it will give error as the script will not be able to get data inside users(the updated directory).

#Some more os module methods-
#os.remove() - removes a file
#os.rmdir() - removes an empty directory
#shutil.rmtree() - deletes a directory and all its content

#NOTE - You can do bulk actions in terms of file reading,renaming etc. in a short span of time using os module.
#There are more methods of os module that one can explore. Aboveare the basic one's one must know.
 