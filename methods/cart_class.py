import sqlite3
import getpass
import os
from Item_class import Item


import sqlite3

class ShoppingCart:
    def __init__(self,connection):
        self.items = []
        self.conn = connection
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS items (itemName TEXT, itemID TEXT, itemDesc TEXT, itemPrice REAL, itemStock INTEGER, itemCategory TEXT)')
    
    def addItem(self, itemName, itemID, itemDesc, itemPrice, itemStock, itemCategory):
        item = Item(itemName, itemID, itemDesc, itemPrice, itemStock, itemCategory)
        self.items.append(item)
        self.cursor.execute('INSERT INTO cart (itemName, quantity) VALUES (?, ?)', (itemName, itemStock))
        self.conn.commit()
        print("Item added to cart and database.")
    def removeItem(self, itemName):
        print(f"Number of items in cart: {len(self.items)}")
        for item in self.items:
            print("I'm in the for loop")
            if item.getitemName() == itemName:
                self.items.remove(item)
                self.cursor.execute('DELETE FROM cart WHERE itemID = ?', (itemName,))
                self.conn.commit()
                print("Item removed from cart and database.")
                break
            else:
                print("Item not found in cart.")
    
    def viewCart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Cart Items: ")
            for item in self.items:
                print(f"{item.getitemName()} ({item.getitemID()}): {item.getitemPrice()}")
    
    def updateQuantity(self, itemID, newStock):
        for item in self.items:
            if item.getitemID() == itemID:
                item.setitemStock(newStock)
                self.cursor.execute('UPDATE items SET itemStock = ? WHERE itemID = ?', (newStock, itemID))
                self.conn.commit()
                print("Quantity updated in cart and database.")
                break
        else:
            print("Item not found in cart.")
    
    def totalPrice(self):
        total = 0
        for item in self.items:
            total += item.getitemPrice()
        return total
    
    def checkout(self):
        self.items.clear()
        self.cursor.execute('DELETE FROM items')
        self.conn.commit()
        print("Cart cleared and items purchased.")

