#write the code to implement factorial of given number

n = int ( input ("Enter the number for factorial: "))
fact = 1

for i in range (1, n + 1):
    fact = fact * i

print ("the factorial of",n ,"is",fact)


#count the number of leap year from starting year to ending year

sty = int (input ("Enter the starting year : "))
edy = int (input ("Enter the ending year : "))
count=0

while sty <= edy:
    if sty % 4 == 0:
        print(sty,"is leap year")
        count += 1
    sty += 1
    
print (count,"is the number of leap years between starting and ending year")


