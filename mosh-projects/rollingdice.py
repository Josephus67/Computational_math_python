import random
choice = input("Do you want to play the dice rollling Game? y/n")
if choice.lower() =='y' :
    choice2= input("do you want to roll the dice? y/n")
    if choice2.lower()=='y':
        dice1=random.randint(1,6)
    else: 
        print("invalid input")
        exit()
    choice3 = input("do you want to roll the second dice? y/n")
    if choice3=='y':
        dice2=random.randint(1,6)
    elif choice3.lower() == 'n':
        print("ok, see you another time")
    else: print("invalid input")
    print(dice1,"and",dice2)
    
elif choice.lower() == 'n':
    print("ok, see you another time")
else: print("invalid input")


import random

choice = input("Do you want to play the dice rolling Game? y/n ")
if choice.lower() == 'y':
    roll_first = input("Roll the first dice? y/n ")
    if roll_first.lower() == 'y':
        dice1 = random.randint(1, 6)
    else:
        print("Ok, see you another time")
        exit()

    roll_second = input("Do you want to roll the second dice? y/n ")
    if roll_second.lower() == 'y':
        dice2 = random.randint(1, 6)
        print(dice1, "and", dice2)
    elif roll_second.lower() == 'n':
        print("Ok, see you another time")
    else:
        print("Invalid input")
elif choice.lower() == 'n':
    print("Ok, see you another time")
else:
    print("Invalid input")