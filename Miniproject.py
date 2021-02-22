import re
Input_file=open("Input.txt")
Keyword=input("Enter the word to search\n")
count=0
for line in Input_file:
    file_line=Input_file.readline()
    match=re.findall(Keyword,file_line,re.M|re.I)
    if match:
        count+=1
        print(line)
        print(file_line)
    else:
        continue
print(count)
Input_file.close()
