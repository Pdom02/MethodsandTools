import sqlite3
from Item_class import Item



class Store:
    
    def __init__(self, adminID, adminPass):
        self.adminID = adminID
        self.adminPass = adminPass

    def setadminID(self, adminUser):
        self.adminID = adminUser
    
    def setadminPass(self, password):
        self.adminPass = password
    
    def getadminID(self):
        return self.adminID
    
    def getadminPass(self):
        return self.adminPass
    
    def removeAccount(self, connection, cursor, customer_rmv):
        cursor.execute("SELECT * FROM Customer")
        rows = cursor.fetchall()
        for row in rows:
            if customer_rmv == str(row[5]):
                cursor.execute("DELETE FROM Customer WHERE customerID=?", (row[5], ))
                print("Item deleted")
                connection.commit()
    def removeListing(self, connection, cursor, rmv_choice):
        cursor.execute("SELECT * FROM Listings")
        rows = cursor.fetchall()
        for row in rows:
            if rmv_choice == str(row[1]):
                cursor.execute("DELETE FROM Listings WHERE item_id=?", (row[1], ))
                print("Item deleted")
                connection.commit()