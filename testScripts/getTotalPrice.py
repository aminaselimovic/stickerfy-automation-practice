import time
from functions import id, quantity, loading
from drivers import *
from selenium.webdriver.common.by import By

loading("TEST 1: Adding to the cart")


driver = headlessChrome()
driver.get("https://stickerfy.herokuapp.com/")
for _ in range(quantity):
    buttons = driver.find_elements(By.LINK_TEXT, "Add to cart")
    addToCartButton = buttons[id-1]
    addToCartButton.click()
    time.sleep(2)
goToCartButton = driver.find_element(By.LINK_TEXT, "Go to cart")
goToCartButton.click()
time.sleep(3)
strongElements = driver.find_elements(By.TAG_NAME, "strong")
for element in strongElements:
    if "Total" in element.text:
        expectedPrice = float(element.text.lstrip("Total: "))

print("-" * 50)

driver.close()