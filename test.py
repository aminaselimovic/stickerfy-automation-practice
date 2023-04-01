import unittest
from drivers import *
from functions import *
from testScripts.getTotalPrice import expectedPrice
from testScripts.removeItem import expectedQuantity
from testScripts.removeAll import zeroQuantity

class TestCheckout(unittest.TestCase):
    def testAddToCart(self):
        result = addToCartFunction(quantity)
        self.assertEqual(result, expectedPrice, "Adds a sticker/stickers to the cart.")
    def testRemoveItem(self):
        result = removeItemFunction(quantity)
        self.assertEqual(result, expectedQuantity, "Removes a sticker from the cart.")
    def testRemoveAllItems(self):
        result = removeAllFunction(quantity)
        self.assertEqual(result, zeroQuantity, "Removes a sticker from the cart.")

if __name__ == "__main__":
    unittest.main()





        