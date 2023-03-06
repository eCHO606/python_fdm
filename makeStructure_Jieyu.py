'''
Name: Jieyu Wang
Project discription of Phase1 : arrange a large collection of files into a new tree structure 
based the year, month, and day.
'''

import os
import shutil
import testSystem
import getpass


def create_base_dir():
    #get the system we are currently in by import testSystem 
    systemType, usersPath = testSystem.switch_system() 
    username = getpass.getuser()
    
    #get all needed path and create the base dir
    user_path = os.path.join(usersPath, username)
    python_data_dir = os.path.join(user_path, "Python_Data")
    base_dir = os.path.join(python_data_dir, "filesToSort")

    return base_dir


def get_dir(filename: str) -> tuple:
    #get the first line from the files
    with open(filename, "r") as f:
        date = f.readline()
    #separate year, month, and day by "-"
    #saved dates as  tuple
    year, month, day = date.strip().split("-")
    return year, month, day


def make_dir(date: tuple, filename: str, base_str: str):
    year, month, day = date
    #create the path hierarchically in order to make the tree-structured dir
    year_path = os.path.join(base_str, year)
    month_path = os.path.join(year_path, month)
    day_path = os.path.join(month_path, day)
    
    old_filepath = os.path.join(base_str, filename)
    new_filepath = os.path.join(day_path, filename)

    
    try:
        #directories are created when needed, check if the directories'name unique
        if not os.path.isdir(year_path):
            os.mkdir(year_path)

        if not os.path.isdir(month_path):
            os.mkdir(month_path)

        if not os.path.isdir(day_path):
            os.mkdir(day_path)

        #move files from the old filepath to the new filepath
        shutil.move(old_filepath, new_filepath)

    except FileExistsError as error:
        print("File already exist", error)


if __name__ == '__main__':
    #run main
    #get the base dir by using create_base_dir function
    base_dir = create_base_dir()

    #Recusively create the files, get the date and create the dir
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            path = os.path.join(root, file)
            if file.startswith("ff_"):
                date = get_dir(path)
                make_dir(date, file, base_dir)
