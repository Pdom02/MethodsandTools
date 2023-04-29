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
    