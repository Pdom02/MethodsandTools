import sqlite3
import getpass
import random
import sys
import os

connection = sqlite3.connect("C:\\Users\\dalen\\OneDrive\\Documents\\GitHub\\MethodsandTools\\MethodsandTools\\Customer\\Customer.db")

class User:
        #constructor
        def __init__ (self):
                
                self.UsrName = ""
                self.Pass = ""
                self.UsrFname = ""
                self.UsrLname = ""
                self.address = ""
                self.shpaddy = ""
                self.email = ""
                self.payhistory = ""

                self.UsrID =  0

        # USERNAME AND PASSWROD
        def setUsrname(self, UsrName):
                self.UsrName = UsrName

        def setPass(self, Pass):
                self.Pass = Pass
        
        def getUsrname(self):
                return self.UsrName

        def getPass(self):
                return self.Pass
        
        #USER ID
        def setID(self, UsrID):
                self.UsrID = UsrID #Generate the user Id in the main when they pick the register

        def getID(self):
                return self.UsrID
        
        #USER NAME (FRIST AND LAST)
        def setFName(self, UsrFname):
                self.UsrFname = UsrFname

        def getFName(self):
                return self.UsrFname
        
        def setLName(self, UsrLname):

                self.UsrLname = UsrLname

        def getLName(self):
                return self.UsrLname

        #USER ADDRESS
        def setAddy(self, address):
                self.address = address
        
        def getAddy(self):
                return self.address
        
        #USER SADDRESS
        def setShpAddy(self, shpaddy):
                self.shpaddy = shpaddy
        
        def getShpAddy(self):
                return self.shpaddy
        
        #EMAIL
        def setEmail(self,email):
                self.email = email

        def getEmail(self):
                return self.email
        
        #Payhistory
        def setpayhis(self, payhistory):
                self.payhistory
        
        def getpayhis(self):
                return self.payhistory
        


        #Controls all of the communication with the database<3
        def register(self):
                username = input("Please enter your Username: ")
                custmr.setUsrname(username)
                password = getpass.getpass("Please enter your Password: ")
                custmr.setPass(password)
                Fname = input("Please enter your First name: ")
                Lname = input("Please enter your Last name: ")
                custmr.setFName(Fname)
                custmr.setLName(Lname)
                addy =  input("Enter your address: ")
                custmr.setAddy(addy)
                custmr.setShpAddy(addy)
                email =  input("Enter your email: ")
                custmr.setEmail(email)
                namepkg = (custmr.getUsrname(), custmr.getPass(), custmr.getFName(),custmr.getLName(), custmr.getAddy(), custmr.getEmail(), custmr.getShpAddy())
                cursor = connection.cursor()
                query = ("INSERT INTO customer (Username, Password, Firstname, Lastname, Age, Address, Email, ShippingAddress) VALUES (?,?,?,?,?,?,?,?)")
                cursor.execute(query,namepkg)
                connection.commit()
        
        def update(self,updatepkg):
                print("Reviewing the UPDATED information:")
                print(updatepkg)
                review = input("Is the information correct? Y or N ")
                if review == 'Y':
                      query = ("UPDATE customer SET Firstname = ? ,  Lastname =?, Address = ?, Email = ?, ShippingAddress = ? WHERE Username = ?") 
                      cursor.execute(query,updatepkg)
        
        def PersInfo(self):
                
                Fname = input("Please enter your First name: ")
                Lname = input("Please enter your Last name: ")
                custmr.setFName(Fname)
                custmr.setLName(Lname)
                addy =  input("Enter your address: ")
                custmr.setAddy(addy)
                custmr.setShpAddy(addy)
                email =  input("Enter your email: ")
                custmr.setEmail(email)
                namepkg = (custmr.getName(), custmr.getAddy(), custmr.getEmail(), custmr.getShpAddy())
                return namepkg                
        
        def login(self):
                username = input("Please enter your Username: ")
                custmr.setUsrname(username)
                password = getpass.getpass("Please enter your Password: ")
                custmr.setPass(password)
                try:
                        cursor.execute("SELECT * FROM Customer WHERE username = ? AND password = ?", (username, password))
                        print("Accepted")
                except:
                        print("Wrong username or password...")


        def editHistory(self):
                print("EDITING: ")
                print("1: Shipping Address")
                print("2: Payment History")
                update = input("Which one do you want to update?")
                if update == "1":
                        shippingadd = input("Please enter your new shipping address:")
                        custmr.setShpAddy(shippingadd)
                        username = custmr.getUsrname()
                        shppkg = (shippingadd, username)
                        print(shippingadd)
                        review = input("Is the information correct? Y or N ")
                        if review == 'Y':
                                query = ("UPDATE customer SET ShippingAddress = ? WHERE Username = ?")
                                cursor.execute(query, shppkg )
                                connection.commit()
               
                elif update == "2":
                        payhis = input("Please enter your new shipping address:")
                        custmr.setpayhis(payhis)
                        username = custmr.getUsrname()
                        paypkg = (payhis, username)
                        print(payhis)
                        review = input("Is the information correct? Y or N ")
                        if review == 'Y':
                                query = ("UPDATE customer SET PaymentHistory = ? WHERE Username = ?")
                                cursor.execute(query, paypkg )
                                connection.commit()
                        
        def delete(self):
                dlt = input("Do you wish to delete? Y/n?")
                if dlt == "Y":
                        username = custmr.getUsrname()
                        cursor.execute("SELECT CustomerID FROM customer WHERE Username = ?", (username))
                        ID = cursor.fetchone()
                        cursor.execute("DELETE FROM customer WHERE CustomerID = ?",[ID])
                        connection.commit()
                else:
                        print("Failed to delete")
               

custmr = User()

quit = 1
while(quit != 0):
        cursor = connection.cursor()
        print("User Choices:\n")
        print("1: Register")
        print("2: View Table")
        print("3: Update Personal Info")
        print("4: Update Payment Info")
        print("5: Login")
        print("6: Quit")
        urs = input("What is your choice? ")
        if urs == "1":
                custmr.register()
                cursor.execute("SELECT * FROM customer")
                print(cursor.fetchall())
                connection.commit()
        elif urs == "2":
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM customer")
                print(cursor.fetchall())
                connection.commit()
        elif urs == "3":
                #Once it logs in check else register
                #In separete menu it can update stuff

                ##connection = sqlite3.connect("C:\\Users\\dalen\\OneDrive\\Documents\\GitHub\\MethodsandTools\\MethodsandTools\\Customer\\Customer.db")
                
                Username = "theo12"
                updatepkg = ('Leo', 'Troy', '123 Simone Strt', 'tasd@gmail.com', 'POBOX 13321', Username)
                custmr.update(updatepkg)
                cursor.execute("SELECT * FROM customer")
                print(cursor.fetchall())
                connection.commit()#  
        elif urs == "4":
              custmr.editHistory()  
        elif urs == "5":
                custmr.login()
        elif urs == "6":
                ID = 2
                custmr.delete()

                

SystemExit
