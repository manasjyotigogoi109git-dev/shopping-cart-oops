#making a BASE CLASS PRODUCT(encapsulation)
from itertools import product


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
    
    def view_cart(self):
     if not self.__items:
        print("🛒 Your cart is empty.")
        return
     print("\n🛒 Cart Contents:")
     for product, quantity in self.__items:
        price = product.get_discounted_price(15)
        print(f"{quantity} x {product.name} @ ₹{price:.2f} each")
    
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
 laptop = Electronics("Laptop", 50000, 50, 2)
 phone = Electronics("phone", 25000, 80, 1)
 shirt = Clothing("Shirt", 800, 10, "Cotton")
 jeans = Clothing("jeans", 1020, 10, "Cotton")
 rice = Groceries("Rice (5kg)", 300, 20)
 atta = Groceries("Atta (5kg)", 180, 50)

 products = [laptop,phone,shirt,jeans,rice,atta]
cart = Cart()


while True:
    print("\n🛒 Welcome to the Store!")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Cart Items")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n📦 Available Products:")
        for i, prod in enumerate(products):
            print(f"{i+1}. ", end="")
            prod.display()

    elif choice == "2":
        prod_num = int(input("Enter product number to add: ")) - 1
        quantity = int(input("Enter quantity: "))
        if 0 <= prod_num < len(products):
            cart.add_products(products[prod_num], quantity)
        else:
            print("Invalid product number.")

    elif choice == "3":
        name = input("Enter product name to remove: ")
        cart.remove_product(name)

    elif choice == "4":
        
        cart.view_cart()

    elif choice == "5":
        cart.checkout()

    elif choice == "6":
        print("Thank you for shopping! 🛍️")
        break

    else:
        print("Invalid choice. Please try again.")

