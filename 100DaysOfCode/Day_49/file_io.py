#There are built-in methods present in python for file handling.
#open() method is used to open a file in python. It takes two parameters, the name of the file and the mode in which the file is opened. The mode can be read, write, append, etc.
f= open('myfile.txt','r')
#The mode in which you are opening the file the same action should be performed like it you open a file in r(read mode) thrn the action performed must be of read as so on.

text = f.read();
print(text)
f.close()

#writing to a file
f = open('myfile2.txt','w')   
f.write('Hello, World!')
f.close()

#appending to a file
f = open('myfile2.txt','a')
f.write('\nThis is an appended line.')
f.close()

#modes in file handling:

#read(r) - Read mode which is used when the file is only being read. It is the default mode if nothing is specified. If the file does not exist, it throws an error.
#write(w) - Write mode which is used to edit and write new information to the file. If the file does not exist, it creates a new file for writing. Also in write mode if the file already exists, it will overwrite the existing content of the file.So if you just want to add content use append().
#append(a) - Append mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end. If the file does not exist, it creates a new file for writing.
#create(x) - Create mode, which is used to create a new file. If the file already exists, the operation will fail and it throws an error.
#text(t) - Text mode which is used to handle files that contain text data. It is the default mode if nothing is specified. r or rt and w or wt are the same.
#binary(b) - Binary mode which is used to handle files that contain binary data (images, audio files, etc.). rb and wb are the same.

#with statement - It is used to open a file and it automatically closes the file after the nested block of code. It is used to avoid memory leaks and to ensure that the file is properly closed after its suite finishes, even if an exception is raised on the way. It is a good practice to use with statement when working with files.
with open('myfile.txt','r') as f:
    print(f.read())

with open('myfile2.txt','a') as f:
    f.write('\nThis is another appended line.')

#NOTE - This is a basic introduction to file handling in python. There are many other methods and functionalities available in python for file handling.

# It is helpful when you want to store data in a file and retrieve it later. It is also helpful when you want to share data between different programs or systems. it canbe used as a temporary local storage for data that is being processed. 
