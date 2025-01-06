inputFile = open('automation/inputFile.txt','r')
#print entire file
#print(inputFile.read())

#print only those who have passed
# for line in inputFile:
#     line_split = line.split()
#     if line_split[2]=='P':
#         print(line)

print("those who have failed")
for line in inputFile:
    line_split = line.split()
    if line_split[2]=='F':
        print(line)

inputFile.close()