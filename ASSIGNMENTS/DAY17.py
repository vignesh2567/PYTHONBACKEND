#TYPES OF INHERITANCE

#MULTIPLE INHERITANCE

class A ():
    def student_details(self):
        self.a = input ("ENTER YOUR NAME:")
        self.b = input ("ENTER YOUR ROLL NO:")

class B ():
    def student_mark(self):
        self.c = int ( input ("ENTER FRONT END MARK: "))
        self.d = int (input ("ENTER PYTHON MARK: "))

class C(A,B):
    def display_student(self):
        self.student_details()
        self.student_mark()
        
        print ("NAME: ",self.a)
        print ("ROLL NO: ",self.b)
        print ("FRONT END MARK:",self.c)
        print ("PYTHON MARK: ",self.d)
        self.avg = (self.c + self.d) // 2
        print ("AVERAGE MARK OF",self.a,"is",self.avg)

student = C()
student.display_student()

#MULTI LEVEL INHERITANCE

class product_list():
    def list(self):
        self.l = {"asus" : 49000,"victus" : 59000,"lenova" : 70000}

class search_product(product_list):
    def search(self):
        self.s = input ("ENTER LAPTOP NAME FOR ITS PRICE(asus,victus,lenova): ")

class amount(search_product):
    def display_amount(self):
        self.list()
        self.search()
        
        if self.s in self.l:
            print ("price of ",self.s,"is",self.l[self.s])
        else:
            print ("inalid product name!!!")

product_amount = amount()
product_amount.display_amount()
