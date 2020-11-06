import sys
import os
import getpass
import time
import keyring
from github import Github

#Input Taken from Powershell Script
newFolder = sys.argv[1]

#github key save in keyring
g = Github(keyring.get_password("gitHub", "Token"))

user = g.get_user()

#GitHub username.  This is used for the Git remote add.
gitUserName = user.login


#I like to create pricate repos. Change to False to create public.
repo = user.create_repo(newFolder, private=True)

#Curent user for my path
currentUser = getpass.getuser()

print(f"Your New project name is: {newFolder}")

os.chdir(f"C:\\Users\\{currentUser}\\Projects\\Python")
os.mkdir(newFolder)

os.chdir(f"C:\\Users\\{currentUser}\\Projects\\Python\\{newFolder}")
os.system("echo %date%  > Readme.md")
os.system("git init")

os.system(f"git remote add origin git@github.com:{gitUserName}/{newFolder}.git")
os.system("git add .")
os.system("git commit -m \"initial commit \" ")
os.system("git branch -M main")
os.system("git push -u origin main")
os.system("code .")