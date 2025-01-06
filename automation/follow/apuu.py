#open the input file

inputFile = open('automation/inputFile.txt','r')

didpass = open('didpass.txt','w')
didfail = open('didfail.txt','w')

for line in inputFile:
    line_split = line.split()
    if line_split[2]=='P':
        didpass.write(line)
    else: didfail.write(line)

#close files
didpass.close()
didfail.close()