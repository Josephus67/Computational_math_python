inputFile = open('automation/inputFile.txt', 'r')
#print(inputFile.read())
#inputFile.close()

for line in inputFile:
    split_line = line.split()
    if split_line[2] == 'P':
        print(split_line)

gross = open('automation/groceries.txt', 'r')
gross_csv = open('automation/groceries.csv', 'r')
print("********************************")

print(gross.read())
print("********************************")
print(gross_csv.read())