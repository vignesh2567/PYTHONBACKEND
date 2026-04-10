
#task 1

ebill = int (input ("Enter total units :"))

if ebill <= 100:
    print ("No amount need to be paid")
elif ebill <= 200:
    print ((ebill - 100) * 2,"is your total amount ")
else:
    print ("unit above 200 is not mentioned")



#task 2

day = int (input ("Enter any number from 1-7 to know the day :"))

match day:
    case 1:
        print ("SUNDAY")
    case 2:
        print ("MONDAY")
    case 3:
        print ("TUESDAY")
    case 4:
        print ("WEDNESDAY")
    case 5:
        print ("THURSDAY")
    case 6:
        print ("FRIDAY")
    case 7:
        print ("SATURDAY")
    case _:
        print ("enter 1-7 number only!!!")
