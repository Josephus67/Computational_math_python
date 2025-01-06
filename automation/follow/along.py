#read from the input file
inputFile = open('automation/inputFile.txt','r')
#write to the pass file and failFile
passFile = open('passFilej.txt','w')
failFile = open('failFilej.txt','w')

for line in inputFile:
    line_split = line.split()
    if line_split[2]=='P':
        passFile.write(line)
    else: failFile.write(line)


inputFile.close()
passFile.close()
failFile.close()