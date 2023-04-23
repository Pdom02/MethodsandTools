#Class for items
import sqlite3

class Item:
    def __init__(self, itemName, itemID, itemDesc, itemPrice, itemStock, itemCategory):
        self.itemName = itemName
        self.itemID = itemID
        self.itemDesc = itemDesc
        self.itemPrice = itemPrice
        self.itemStock = itemStock
        self.itemCategory = itemCategory
    
    def getitemName(self):
        return self.itemName
    
    def getitemID(self):
        return self.itemID
    
    def getitemDesc(self):
        return self.itemDesc
    
    def getitemPrice(self):
        return self.itemPrice
    
    def getitemStock(self):
        return self.itemStock
    
    def getitemCategory(self):
        return self.itemCategory
    
    def setitemStock(self, newStock):
        self.itemStock = newStock
        
    def setitemCategory(self, newCategory):
        self.itemCategory = newCategory
        
    def setitemName(self, newName):
        self.itemName = newName
        
    def setitemID(self, newID):
        self.itemID = newID
        
    def setitemDesc(self, newDesc):
        self.itemDesc = newDesc
        
    def setitemPrice(self, newPrice):
        self.itemPrice = newPrice


def add_item(item):
    conn = sqlite3.connect("items.db")
    c = conn.cursor()
    c.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?, ?)",
              (item.itemName, item.itemID, item.itemDesc, item.itemPrice, item.itemStock, item.itemCategory))
    conn.commit()
    conn.close()