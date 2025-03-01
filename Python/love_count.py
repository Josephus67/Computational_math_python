def loveCalc():
    bride = str(input('What is the name of the bride'))
    groom = input('what is the name of the groom')
    if len(bride)<=2 or len(groom)<=2:
        return f"names of {bride} and {groom} must be more than 2 characters in Length"
    couple = bride+groom
    
    bride_t = couple.lower().count('t')
    bride_r = couple.lower().count('r')
    bride_u = couple.lower().count('u')
    bride_e = couple.lower().count('e')
    bride_l = couple.lower().count('l')
    bride_o = couple.lower().count('o')
    bride_v = couple.lower().count('v')

    bride_count = bride_t +bride_r+bride_u+bride_e+bride_l+bride_o+bride_v
    love_perc = (bride_count/len(couple))*100
    return love_perc
loveCalc()