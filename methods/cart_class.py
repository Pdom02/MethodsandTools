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
        self.cursor.execute('INSERT INTO cart (itemID, quantity) VALUES (?, ?)', (itemName, itemStock))
        self.conn.commit()
        print("Item added to cart and database.")

    def removeItem(self, rmv_item):
        self.cursor.execute("SELECT * FROM cart WHERE cartID=?", (rmv_item,))
        rows = self.cursor.fetchall()
        if not rows:
            print("Item not found in cart.")
            return
        for item in self.items:
             if item.getitemName() == rmv_item:
                 self.items.remove(item)
        self.cursor.execute('DELETE FROM cart WHERE cartID = ?', (rmv_item,))
        self.conn.commit()
        print("Item removed from cart and database.")

    
    def viewCart(self):
        if not self.items:
            print("Cart is empty.")
            return
        else:
            self.cursor.execute("SELECT * FROM cart")
            rows = self.cursor.fetchall()
            if len(rows) == 0:
                print("Your cart is empty.")
            else:
                for row in rows:
                    print()
                    print("Item ID: ", row[0])
                    print("Name:", row[1])
                    print("Quantity:", row[2])
            
            print("\n0. Return")
            print("1. Remove an item from cart")
            print("2. Checkout\n")
            choice = int(input("Enter your choice: "))
            if choice == 0:
                return
            elif choice == 1:
                rmv_item = int(input("Enter the item ID of the item that you would like to remove from the cart\nIf you would like to go back, enter '0': "))
                if rmv_item == 0:
                    return
                else:
                    for row in rows:
                        if rmv_item == row[0]:
                            self.removeItem(rmv_item)
            elif choice == 2:
                self.checkout()
    
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
    
    # def checkout(self):
    #     self.items.clear()
    #     self.cursor.execute('DELETE FROM items')
    #     self.conn.commit()
    #     print("Cart cleared and items purchased.")
    def checkout(self):
        for item in self.items:
        # Update the stock of each item in the database
            self.cursor.execute('UPDATE Listings SET itemStock = itemStock - ? WHERE itemName = ?', (item.getitemStock(), item.getitemName()))
            self.conn.commit()

    # Clear the cart
        self.items.clear()
        self.cursor.execute("DELETE FROM cart")
    # Commit the changes to the database
        self.conn.commit()
    
        print("Cart cleared and items purchased.")


