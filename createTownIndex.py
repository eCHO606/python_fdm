import os
import testSystem

'''
Project discription of phase 3a : create a file index that
will contain a list of towns and the files that are associated with that town
'''

def create_base_dir():
    systemType, usersPath = testSystem.switch_system()
    username = os.getlogin()

    user_path = os.path.join(usersPath, username)
    python_data_dir = os.path.join(user_path, "Python_Data")
    base_dir = os.path.join(python_data_dir, "filesToSort")

    try:
        if not os.path.isdir(user_path):
            os.mkdir(user_path)

        if not os.path.isdir(python_data_dir):
            os.mkdir(python_data_dir)

        if not os.path.isdir(base_dir):
            os.mkdir(base_dir)

        return True, base_dir
    except Exception as e:
        print(e)
        return False, base_dir


class IndexHandler(object):
    def __init__(self):
        self.__data = []

    def read_file(self):
        flag, base_dir = create_base_dir()
        if flag:
            for root, dirs, files in os.walk(base_dir):
                for file in files:
                    path = os.path.join(root, file)
                    if file.startswith("ff_"):
                        self.get_population(path)

    def get_population(self, filename: str):
        with open(filename, "r") as f:
            data = f.readlines()

        town = data[2].strip()
        try:
            temp = town + ":./" + "/".join(filename.split("\\")[-4:])
            self.__data.append(temp)

        except Exception as e:
            print(e)

    def sort(self):
        self.__data.sort()

    def write_file(self):
        with open(os.path.join(os.path.dirname(__file__), "townFileIndex.txt"), "w") as f:
            for i in self.__data:
                f.write(i)
                f.write("\n")


if __name__ == '__main__':
    handler = IndexHandler()
    handler.read_file()
    handler.sort()
    handler.write_file()
