'''
Discription:This file contains the code to count the Keywords in file
Author:Sushma
Date:22/02/2021
'''
import re
Input_file=open("Input.txt")
Keyword=input("Enter the word to search\n")
count=0
read_file=Input_file.read()
match=re.findall(Keyword,read_file,re.M|re.I)
if match:
    print(len(match))
'''Input_file.close()
Input_file=open("Input.txt")
file_line=Input_file.readlines()
for line in file_line:
    match=re.findall(Keyword,line,re.M|re.I)
    if match:
        count+=1
        print(line)
        print(file_line)
print(count)
Input_file.close()'''
Output_file_name=Keyword+".txt"
Output_file=open(Output_file_name,"w")
Output_file.write(str(len(match)))
Input_file.close()
Output_file.close()
