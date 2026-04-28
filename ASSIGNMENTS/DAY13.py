
#1no parameter,no return

def doubledigit1():
    d=99
    if d > 9 and d < 100:
        print ("THIS IS A VALID DOUBLE DIGIT")
    else:
        print ("THIS AIN'T A DOUBLE DIGIT")

doubledigit1()

#2 with parameter,no return

def doubledigit2(dd):
    if dd > 9 and dd < 100:
        print ("THIS IS A VALID DOUBLE DIGIT")
    else:
        print ("THIS AIN'T A DOUBLE DIGIT")

doubledigit2(1)

#3 with parameter , with return

def doubledigit3(digit):
    if digit > 9 and digit < 100:
        return "THIS IS A VALID DOUBLE DIGIT"
    else:
        return "THIS AIN'T A DOUBLE DIGIT"

op = doubledigit3(33)
print (op)

#4 no parameter ,with return

def doubledigit4():
    num = 1000
    if num > 9 and num < 100:
        return "THIS IS A VALID DOUBLE DIGIT"
    else:
        return "THIS AIN'T A DOUBLE DIGIT"

res = doubledigit4()
print (res)
