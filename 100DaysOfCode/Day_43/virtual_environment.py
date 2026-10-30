#Virtual Environment is a tool used to isloate specific Python environments on a single machine, allowing you to work on multipleprojects with different depedencies and packages without conflicts.

#A virtual environment is an isolated Python environment that maintains its own Python interpreter #reference and installed packages, allowing different projects to use different package versions without #interfering with each other.

#It helps you separate your virtual environment.
#For eg. Suppose you have pandas version 1 and your friend has pandas version 2 then how will you you run his project overyuor system?You will create a virtual environment for version 1 and a virtual environment for version 2.

#This can be specifically useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

#Suppose you have package A and it depends on package B's version 1. When I update package A it starts to depend on package B's version 2.
#So you have to take an environment and I can install all the packages I want and those package version's installed will have nothing to do with your system's python version.

#To create a virtual environment in Python, you can use the venv module that comes with python. 
#Way 1
# Run below commands in cmd prompt -> 
# Create a virtual environment -> python -m venv myenv
# Activate the virtual environment(Windows) ->
# (1)For cmd prompt -> myenv\Scripts\activate.bat  (2) for powershell -> .\myenv\Scripts\Activate.ps1
# Deactivate virtual environment -> deactivate

#Way 2
#You can also creat virtual environment by creating folder directly in your pc and run commands in the cmd prompt.
#STEPS
#-->Create a folder (say python-venv)
#-->Open File Explorer (Win + E) -> Navigate to the folder where you want to open CMD ->Click the address bar at the top -> Type cmd -> Press Enter

#(1) RUN "python3 -m venv myenv" AND A FOLDER NAMED MYENV IS CREATED INSIDE YOUR FOLDER WHICH IS THE COPY OF THE PYTHON IN YOUR PC. NOW YOU CAN PUT ANY ONE VERSION OF ANY PACKAGE AND ANOTHER VERSION OF ANOTHER PACKAGE. 
#(2) But if we run a cmd "pip3 install pandas" it shows requirement already satisfied because it is installing the pandas already present in your PC.

#(3) But you want to install pandas inside "myenv" because my globalenvironment(my pc) already has pandas installed and that is why on running "pip3 install pandas" shows requirement already satisfied.

#(4) Now what we want is to activate this virtual environment.Run "source/myenv/bin/activate" and then you see (myenv) displayed just at the start of your next line where you write cmds.And now when you run "pip" cmd, it will install pandas in this virtual environment and any python program executed runs in this virtual environment.