"""
Discription:This file contains the code to count the Keywords in file
Author:Sushma
Date:22/02/2021
"""
import re
class myclass:
    def __init__(self):
        self.Keyword=input("Enter keyword\n")
        self.Output_file_name = self.Keyword+".txt"
        self.Input_file=open("Input.txt","r")
        self.Output_file = open(self.Output_file_name, "w")
        self.count=0
    def File_read(self):
        file_read=self.Input_file.read()
        file=file_read.split()
        file1=re.split(r"\W",str(file))
        return file1
    def Match_Keyword(self,file1):
        for i in range(len(file1)):
            match=re.fullmatch(self.Keyword,file1[i],re.M|re.I)
            if match:
                self.count+=1 
                str1=file1[i-8]+" "+file1[i-4]+" "+file1[i]+" "+file1[i+4]+" "+file1[i+8]+" "
                self.Output_file.write(str(str1))
                self.Output_file.write("\n")
        self.Output_file.write(str(self.count))
    def Close_file(self):
        self.Input_file.close()
        self.Output_file.close()
myobj=myclass()
file1=myobj.File_read()
myobj.Match_Keyword(file1)
myobj.Close_file()