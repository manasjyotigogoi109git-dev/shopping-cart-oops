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
        

class Cart:
    def __init__(self):
        self.__items = []  # Private list of tuples: (Product, quantity)

    def add_products(self,product,quantity):
        if product.get_stock() >= quantity:
            product.reduce_stock(quantity)
            self.__items.append((product,quantity))
            print(f"Added {quantity} x {product.name} to the cart")
        else:
            print(f"Not enough stock of the product {product.name}")


    def remove_product(self,product_name):
        for i,(prod,qty) in enumerate(self.__items):
            if prod.name == product_name:
                product_name.reduce_stock(-qty)
                del self.__items[i]
                print(f"Removed {product_name} from cart")
                return
            print(f"{product_name} not found in cart")
    
