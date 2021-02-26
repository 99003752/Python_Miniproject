"""
File Name:Miniproject.py
Description:This file contains the code to count the Keywords in file
Date:22/02/2021
Author:Sushma
PS number:99003752
"""
import re  # Importing Regular expression module


class Myclass:  # Class for file handling

    def __init__(self, keyword2):  # instance
        self.Keyword = keyword2  # Keyword to search
        self.Input_file = open("Input.txt", "r")  # Open Input fine
        self.count = 0
        self.Output_file_name = self.Keyword+".txt"
        self.Output_file = open(self.Output_file_name, "w")


class Readclass(Myclass):  # Class to read the file

    def file_read(self):  # method to read file
        file_read = self.Input_file.read()
        file = file_read.split()
        file1 = re.split(r"\W+", str(file))
        return file1  # return List


class Matchclass(Readclass):  # Class to Match Keyword
    def match_keyword(self, file1):  # Method to Match the keyword
        for i in range(len(file1)):
            match = re.fullmatch(self.Keyword, file1[i], re.M | re.I)
            if match:
                self.count += 1  # increment counter if Keyword is found
                str1 = file1[i-1]+" "+file1[i]+" "+file1[i+1]+" "
                self.Output_file.write(str(str1))  # writing into output file
                self.Output_file.write("\n")
        self.Output_file.write("Total number of "+self.Keyword+" Found are ")
        self.Output_file.write(str(self.count))

    def close_file(self):  # Method to close all the files
        self.Input_file.close()
        self.Output_file.close()


if __name__ == "__main__":
    number = input("How many keywords you want to enter\n")
    flag = True
    while flag:
        if number.isdigit():
            number = int(number)
            flag = False
            while number != 0:
                keyword = input("Enter Keyword\n")  # Taking input from user
                myobj = Myclass(keyword)  # Creating object to class
                myobj1 = Readclass(keyword)
                myobj2 = Matchclass(keyword)
                file2 = myobj1.file_read()
                myobj2.match_keyword(file2)
                number -= 1
                myobj2.close_file()
        else:
            print("Enter Valid Input\n")
            number = input("How many keywords you want to enter\n")
