class Product:

    def __init__(self,product_name,price):
        self.product_name = product_name
        self.price=price

    def display_product(self):
        print("the name of the product is:",self.product_name)
        print("the price of the product is:",self.price)

class ElectronicProduct(Product):

    def __init__(self,product_name,price,brand,warranty):
        super().__init__(product_name,price)
        self.brand=brand
        self.warranty=warranty
        
    def display_electronic_product(self):
        print("the brand of the device is:",self.brand)
        print("the warranty for the device is:",self.warranty)

class MobilePhone(ElectronicProduct):
     def __init__(self,product_name,price,brand,warranty,ram,storage):
         super().__init__(product_name,price,brand,warranty)
         self.ram=ram
         self.storage=storage
         
     def display_mobile_details(self):
        print("the ram of the mobile phone is :",self.ram)
        print("the storage of the mobile phone is:",self.storage)

obj=MobilePhone("OPPO","15000","Mobile","2 years","4gb","125gb")
obj.display_mobile_details()
obj.display_electronic_product()
obj.display_product()





























