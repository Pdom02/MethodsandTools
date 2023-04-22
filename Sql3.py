import sqlite3
import getpass
import uuid
import os


sqliteConnection = sqlite3.connect('User_datab.db')

class User:
        #constructor
        def __init__ (self, UsrAge, UsrName,address,UsrID):
                self.UsrAge = UsrAge
                self.UsrName = UsrName
                self.address = address
                self.UsrID =  UsrID


        #setter = age
        def setAge(self, UsrAge):
                self.UsrAge = UsrAge

        def getAge(self):
                return self.UsrAge

        def RandId(self):
                print 
