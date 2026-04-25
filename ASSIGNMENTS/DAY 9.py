#TUPLE CHARACTERISTICS

tuplee=(12,23,34,45,67)

#print using for
for t in tuplee:
    print (t)

#print using while
i=0
while i <len(tuplee):
    print (tuplee[i])
    i += 1

#can save different data types
dt=(1,"two",3.0,True)
print (dt)

#allow duplicates
dup = (1,2,2,3,3,3,4,4,4,4)
print (dup)

#can perform slicing
print ("Sliced parts:",tuplee[2:4])
print ("Sliced parts:",tuplee[-5:-1])
print ("Sliced parts:",tuplee[::-1])

#SET characteristics
'''
1)allosw dyanamic memory allocation
2)dont suppot slicing
'''
sett={12,23,34,45,56,67,78,89,00}

sett.add(11)
print (sett)
sett.remove(67)
print (sett)

#duplicates not supported & different data types will be supported
diff = {1,2,2,3,3,3,4,4,4,4,"five",6.00,True}
print (diff)

dif = {2,3,4,"five",6.00,True,False}
print (dif)
