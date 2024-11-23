import random

my_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

number_of_passwords = int(input("Number of passwords"))
length_of_password = int(input("Length of each password"))

for i in range(number_of_passwords):
    passwords = ''
    for j in range(length_of_password):
        passwords += random.choice(my_list)
    print(passwords)


# print all possible passwords

def password(x: int):
    from string import digits
    for i in digits:
        for j in digits:
            for k in digits:
                for l in digits:
                    for m in digits:
                        for n in digits:
                            print(i + j + k + l + m + n)

password(6)