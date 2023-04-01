import time
from functions import id, quantity, loading
from drivers import *
from selenium.webdriver.common.by import By

loading("TEST 2: Removing item")

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
dropdown = driver.find_element(By.CSS_SELECTOR, "button[data-toggle='dropdown']").click()
time.sleep(2)
remove1Button = driver.find_element(By.LINK_TEXT, "Remove 1").click()
time.sleep(3)
currentQuantity = driver.find_element(By.XPATH, "//span[@class='badge']")
expectedQuantity = int(currentQuantity.text)

print("-" * 50)

driver.close()