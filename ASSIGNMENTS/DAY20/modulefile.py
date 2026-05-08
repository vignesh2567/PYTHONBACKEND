#MODULE FILE

data = {"name":"vicky","id":1138,"degree":"BCA"}

def oddeven(n):
    if n // 2 == 0:
        print ("EVEN Number")
    else:
        print ("ODD Number")

class avg():
    def value(self):
        self.a = int(input("enter first value: "))
        self.b = int (input ("enter second value: "))
        self.c = int (input("enter third value: "))

    def calc(self):
        self.d = (self.a+self.b+self.c)//2
        print ("The average value is",self.d)

