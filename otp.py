import random
def genotp():
    ul=[chr(i) for i in range(ord("A"),ord("Z")+1)]  #chr(65) ,capital letters list
    sl=[chr(i) for i in range(ord("a"),ord("z")+1)]  #small letters list
    otp=""
    for i in range(2):  #it has to iterate for 2 times,as our requirement is 6digits
        otp=otp+str(random.randint(0,9))   #as otp is string format we cannot add numbers to string,so we convert using str
        otp=otp+random.choice(ul)  #random.choice will randomly pick 2num
        otp=otp+random.choice(sl)
    return otp