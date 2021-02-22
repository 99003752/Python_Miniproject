import re
Input_file=open("Input.txt")
count=0
for line in Input_file:
    file_line=Input_file.readline()
    match=re.search("software",file_line,re.M|re.I)
    if match:
        count+=1
       # print(line)
        print(file_line)
    else:
        continue
print(count)
Input_file.close()
