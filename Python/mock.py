
'''def mod_random(a, b):
    import random
    modr = a + (b - a) * random.random()
    lst = []
    while len(lst) < 10:
        lst.append(modr)
    print(lst)

mod_random(-1, 2)
'''
def rand_num (a,b):
    import random
    random_num= a + (b-a)*random.random()
    list=[]
    while (len(list)<10):
        list.append(random_num)
    print(list)
    
rand_num(1,4)
#hello world