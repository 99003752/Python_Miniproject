"""
Discription:This file contains the code to count the Keywords in file
Author:Sushma
Date:22/02/2021
"""
import re
import os
class myclass: 
    def __init__(self,Keyword):
        self.Keyword=Keyword
        self.Input_file=open("Input.txt","r")
        self.count=0
        self.Output_file_name = self.Keyword+".txt"
        self.Output_file = open(self.Output_file_name, "w")
    def File_read(self):
        file_read=self.Input_file.read()
        file=file_read.split()
        file1=re.split(r"\W+",str(file))
        return file1
    def Match_Keyword(self,file1):
        for i in range(len(file1)):
            match=re.fullmatch(self.Keyword,file1[i],re.M|re.I)
            if match:
                self.count+=1 
                str1=file1[i-1]+" "+file1[i]+" "+file1[i+1]+" "
                self.Output_file.write(str(str1))
                self.Output_file.write("\n")
        self.Output_file.write("Total number of "+self.Keyword+" Found are ")
        self.Output_file.write(str(self.count))
    def Close_file(self):
        self.Input_file.close()
        self.Output_file.close()
if __name__=="__main__":
    number=int(input("How many keywords you want to enter\n"))
    while number!=0:
        Keyword=input("Enter Keyword\n")
        myobj=myclass(Keyword)
        file1=myobj.File_read()
        myobj.Match_Keyword(file1)
        number-=1
    myobj.Close_file()
