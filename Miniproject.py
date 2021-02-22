'''
Discription:This file contains the code to count the Keywords in file'''
import re
Input_file=open("Input.txt")
Keyword=input("Enter the word to search\n")
count=0
read_file=Input_file.read()
match=re.findall(Keyword,read_file,re.M|re.I)
if match:
    print(len(match))
#file_line=Input_file.readlines()
#for line in file_line:
#    match=re.findall(Keyword,line,re.M|re.I)
#    if match:
 #       count+=1
       # print(line)
       # ripnt(file_line)
#print(count)
Input_file.close()
