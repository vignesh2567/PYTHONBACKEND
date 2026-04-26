#1) write a code to print the biggest number from the list [100,230,45,564, 76]

numbers = [100,230,45,564, 76,1000]

big = numbers[0]
for n in numbers:
    if n > big:
        big = n
print ("Biggest number is:",big)


#2)write a code to find the no of occurances of given number [10,20,30,10,20,40,50,50]

numbers = [10, 20, 30, 10, 20, 40, 50, 50]

count = {}
for num in numbers:
    count[num] = count.get(num, 0) + 1

x = int(input("Enter a number from [10, 20, 30, 10, 20, 40, 50, 50 ]: "))

if x in count:
    print(x, "occurs", count[x], "times")
else:
    print(x, "does not exist in the list")
