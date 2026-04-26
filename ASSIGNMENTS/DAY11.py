#give any 2 realtime example for list, tuple, set

#LIST
list = [1,"one",1.0,True]   #support duplicate values
print (list)

list.append("two")  #allow dynamic memory location
print (list)

print (list[3])

#TUPLE

tuple = ("a1","b2","c3",1,2,3)
print (tuple)
print (tuple[2])    #allows slicing
print(tuple.add(True))  #Doesn't allow  DYNAMIC MEMORY LOCATION

#SET

set = {"zero","one",2,3,True, False,3,True}
print(set)  #unordered storing,allow multiple data  types and remove duplicates
print (set[1])  #doesn't support slicing cause doesn't have index
