
# VIRTUAL  FUNCTION AND FUNCTION OVERRIDING

class product():

    def product_list(self):                                  # virtual function
        self.pl = ("ASUS","VICTUS","LENOVA","ACER","DELL")   #old product list

    def available_product(self):                             #virtual function
        print ("Available products are :")                   #to display products in the list
        for self.ap in self.pl:
            print (self.ap)

class productv2(product):
    def product_list(self):                                  #function overriding
        print ("UPDATED PRODUCTS LIST!!!")
        self.pl = ("ASUS F17","HP","MAC BOOK PRO","SEPARATE OLED MONITOR")  #updated list
    

obj = productv2()
obj.product_list()
obj.available_product()
