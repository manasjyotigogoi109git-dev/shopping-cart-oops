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
        return discounted
    

class Clothing(Product):
    def __init__(self,name,price,stock,material):
        super().__init__(name,price,stock)
        self.material = material
    
    def display(self):
        super().display()
        print(f"Material:{self.material}")

    def get_discounted_price(self,discount_percent):
        discounted = self.get_price() * (1-discount_percent/100)
        return discounted

class Groceries(Product):
    def __init__(self,name,price,stock):
        super().__init__(name,price,stock)
        
    
    def display(self):
        super().display()
        

    def get_discounted_price(self,discount_percent):
        discounted = self.get_price() * (1-discount_percent/100)
        return discounted
        

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
                prod.reduce_stock(-qty)
                del self.__items[i]
                print(f"Removed {product_name} from cart")
                return
        print(f"{product_name} not found in cart")
    
    def checkout(self):
        total=0
        print("\n Reciept:")
        for product,qty in self.__items:
            discount = product.get_discounted_price(15)
            line_total = discount * qty
            total+= line_total
            print(f"{qty} x {product.name} @₹{discount} = ₹{line_total}")
        print(f"\n total amount is: ₹ {total}")


if __name__ == "__main__":
    # Create products
 laptop = Electronics("Laptop", 50000, 5, 2)
 shirt = Clothing("Shirt", 800, 10, "Cotton")
 rice = Groceries("Rice (5kg)", 300, 20)
 atta = Groceries("Atta (5kg)", 180, 50)

# Display products
laptop.display()
shirt.display()
rice.display()

# cart instacne
cart = Cart()

#objects
cart.add_products(laptop, 3)
cart.add_products(shirt, 2)
cart.add_products(rice, 3)
cart.add_products(atta, 5)

# Remove one item
cart.remove_product("Shirt")

# Checkout
cart.checkout()