'''
Name:Jieyu Wang
Project discription: report the population statistics by year.
'''

import os
import sys
import makeStructure_Jieyu


class PopulationHandler(object):
    #collect the data needed from files
    def __init__(self):
        self.__data = {}

    def read_file(self):
        #read the file from the module created at phase1
        base_dir = makeStructure_Jieyu.create_base_dir()
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                path = os.path.join(root, file)
                if file.startswith("ff_"):
                    self.get_population(path)

    def get_population(self, filename: str):
        with open(filename, "r") as f:
            data = f.readlines()

        year, month, day = data[0].strip().split("-")
       
        try:
             #get population from the last line
            population = int(data[-1].strip())

            #append exist date and population together to help with choosing by userself
            if year in self.__data:
                self.__data[year].append(population)
            else:
                self.__data[year] = []
        except Exception as e:
            print(e)

    def sub_menu(self):
        #let user select the key words from the years list
        year = input("Please input year you want to stat (2000 - 2019): ")

        if year not in self.__data:
            print("The data of the year you just input does not exit!")
        
        #if the year dir exist, then input the calculation keyword
        else:
            keyword = input("Please input keyword (sum, average, minimum, maximum, all or exit): ")
            #calculate by sum, average, minimum, maximum and all.
            if keyword == "sum":
                print("The total population for the year {} was {}".format(year, sum(self.__data[year])))
            elif keyword == "average":
                print("The average population for the year {} was {}".format(year, int(sum(self.__data[year]) / len(self.__data[year]))))
            elif keyword == "minimum":
                print("The minimum population for the year {} was {}".format(year, min(self.__data[year])))
            elif keyword == "maximum":
                print("The maximum population for the year {} was {}".format(year, max(self.__data[year])))
            elif keyword == "all":
                print("The total population for the year {} was {}".format(year, sum(self.__data[year])))
                print("The average population for the year {} was {}".format(year, int(sum(self.__data[year]) / len(self.__data[year]))))
                print("The minimum population for the year {} was {}".format(year, min(self.__data[year])))
                print("The maximum population for the year {} was {}".format(year, max(self.__data[year])))
            
            #if input exit, than system exit by import the sys module.
            elif keyword == "exit":
                sys.exit(0) 
            #otherwise send the error message
            else:
                print("The keyword is not one of those listed!")


if __name__ == '__main__':
    handler = PopulationHandler()
    handler.read_file()
    while True:
        handler.sub_menu()
