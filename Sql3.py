import sqlite3
import getpass
import random
import sys
import os



class User:
        #constructor
        def __init__ (self):
                self.UsrAge = 0
                #self.UsrName = ""
                self.UsrFname = ""
                self.UsrLname = ""

                self.address = ""
                #self.shpaddy = ""
                self.email = ""

                self.UsrID =  0


        #USER AGE
        def setAge(self, UsrAge):
                self.UsrAge = UsrAge
        
        def getAge(self):
                return self.UsrAge

        #USER ID
        def setID(self, UsrID):
                self.UsrID = UsrID #Generate the user Id in the main when they pick the register

        def getID(self):
                return self.UsrID
        
        #USER NAME (FRIST AND LAST)
        def setName(self, UsrFname, UsrLname):
                self.UsrFname = UsrFname
                self.UsrLname = UsrLname

        def getName(self):
                return self.UsrFname, self.UsrLname
        
        #USER ADDRESS
        def setAddy(self, address):
                self.address = address
        
        def getAddy(self):
                return self.address

        #EMAIL
        def setEmail(self,email):
                self.email = email

        def getEmail(self):
                return self.email
        
        '''  #SHIP ADDRESS
        def setShipAd(self, shpaddy):
                self.shpaddy = shpaddy
        
        def getShipAd(self):
                return self.shpaddy'''
        

custmr = User()

quit = 1
while(quit != 0):
        print("User Choices:\n")
        print("1: Add Name")
        print("2: Add Age")
        print("3: Add Address") #Assuming that the shipping address and the address are the same
       # print("4: Add Shipping Address")
        print("4: Add Email")
        print("5: Review")
        print("6: Quit")
        urs = input("What is your choice? ")
        if urs == "1":
                Fname = input("Please enter you First name: ")
                Lname = input("Please enter you Last name: ")
                custmr.setName(Fname, Lname)      
                print("The name is", custmr.getName())
        elif urs == "2":
                age = input("Please enter your age: ")
                custmr.setAge(age)
                print("Your Age is: ", custmr.getAge())         
        elif urs == "3":
                addy =  input("Enter your address: ")
                custmr.setAddy(addy)
                print("You address is: ", custmr.getAddy())
        elif urs == "4":
                email =  input("Enter your email: ")
                custmr.setEmail(email)
                print("You email address is: ", custmr.getEmail())
        elif urs == "5":
              print("Review Data:")
              print("First name: ", Fname)
              print("Last name: ", Lname)
              print("Age: ", age )
              print("Email: ", email)
              print("Address: ", addy)
              
              review = input("Is the information correct? Y or N ")
              if review == 'Y':
                      namepkg = (Fname, Lname, age, email, addy)
                      query = ("INSERT INTO Customer (Firstname, Lastname, Age, Address, Email) VALUES (?,?,?,?,?)") 
                      cursor.execute(query,namepkg)
                      
              else:
                        break
                      
                      
        elif urs == "6":
                try:
                        connection = sqlite3.connect("Customer.db")
                        print("Successful connection.")

                except:
                        print("Failed connection.")

                        ## exits the program if unsuccessful
                        sys.exit()


                cursor = connection.cursor()
                query = ("INSERT INTO customer (Firstname, Lastname, Age, Address, Email) VALUES (?,?,?,?,?)") 
                namepkg = ('Theo', 'Angeles', '12', '123 Simone Ln', 'ta@gmail.com')
                cursor.execute(query,namepkg)
                        
