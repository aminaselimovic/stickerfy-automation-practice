import time
from drivers import *
from selenium.webdriver.common.by import By

allProducts = {"Product 1": {"Product ID": 1, "Product Name": "Happy", "Product Price": 5.5},
               "Product 2": {"Product ID": 2, "Product Name": "Sad", "Product Price": 7},
               "Product 3": {"Product ID": 3, "Product Name": "Angry", "Product Price": 4.5}
               }

def loading(title):
    i = 10
    seconds_between_iterations = 3
    character = "."
    print(title, end="")

    for _ in range(i):
        time.sleep(seconds_between_iterations)
        print(character, end="", flush=True)

    print()

def listProducts():
    for i in range(len(allProducts)):
        print("Product ID:", allProducts[f"Product {i+1}"]["Product ID"])
        print("Product Name:", allProducts[f"Product {i+1}"]["Product Name"])
        print("Product Price:", allProducts[f"Product {i+1}"]["Product Price"])
        print("-" * 50)

listProducts()

id = int(input("Please enter the ID of the product you want to add to the cart: "))
quantity = int(input("Please enter the quantity: "))
print("-" * 50)

def addToCartFunction(quantity):
    if id <= len(allProducts):
        productPrice = float(allProducts[f"Product {id}"]["Product Price"])
        totalPrice = productPrice * quantity
        totalPrice = float(totalPrice)
        return totalPrice
    else:
        print("No such ID!")

def removeItemFunction(quantity):
    if id <= len(allProducts):
        quantity -= 1
        return quantity
    else:
        print("No such ID!")

def removeAllFunction(quantity):
    if id <= len(allProducts):
        quantity = 0
        return quantity
    else:
        print("No such ID!")
