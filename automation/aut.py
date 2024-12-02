inputFile = open('automation/inputFile.txt', 'r')
#print(inputFile.read())

# for line in inputFile:
#     split_line = line.split()
#     if split_line[2] == 'P':
#         print(split_line)



gross = open('automation/groceries.txt', 'r')
gross_csv = open('automation/groceries.csv', 'r')
print("********************************")

print(gross.read())
print("********************************")
print(gross_csv.read())

#pass files and writing files
passFile = open('automation/passFile.txt', 'w')

failFile = open('automation/failFile.txt', 'w')

for line in inputFile:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)

inputFile.close()


passFile.close()
failFile.close()