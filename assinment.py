#making a BASE CLASS PRODUCT(encapsulation)
class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def get_price(self):#getter method as it is a private
        return self.__price
    
    def get_stock(self):
        return self.__stock
    
    def reduce_stock(self,quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            print(f"Not enough stock for {self.name}") 
    def display(self):
     print(f"{self.name}: ₹{self.__price}, Stock: {self.__stock}")


class Electronics(Product):
    def __init__(self,name,price,stock,warrenty_years):
        super().__init__(name,price,stock)
        self.warrenty_years = warrenty_years
    
    def display(self):
        super().display()
        print(f"Warrenty:{self.warrenty_years} years")

    def get_discounted_price(self,discount_percent):
        discounted = self.get_price() * (1-discount_percent/100)
        print(f"discounted price is {discounted}")
    

class Clothing(Product):
    def __init__(self,name,price,stock,material):
        super().__init__(name,price,stock)
        self.material = material
    
    def display(self):
        super().display()
        print(f"Material:{self.material}")

    def get_discounted_price(self,discount_percent):
        discounted = self.get_price() * (1-discount_percent/100)
        print(f"discounted price is {discounted}")

class Groceries(Product):
    def __init__(self,name,price,stock):
        super().__init__(name,price,stock)
        
    
    def display(self):
        super().display()
        

    def get_discounted_price(self,discount_percent):
        discounted = self.get_price() * (1-discount_percent/100)
        print(f"discounted price is {discounted}")
        




#testcode
if __name__ == "__main__":
    items = [ 
        Electronics("Laptop",75000,30,3),
        Clothing("Jeans",900,20,'cotton'),
        Groceries("potato",30,200)
    ]

for item in items:
     item.display()
     item.get_discounted_price(15) # Apply 15% discount 
     print("---")
