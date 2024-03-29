import getpass
import sqlite3

class User():
        #constructor
        def __init__ (self, connection):
                self.connection = connection
                self.UsrName = ""
                self.Pass = ""
                self.UsrFname = ""
                self.UsrLname = ""
                self.UsrAge = 0
                self.address = ""
                self.shpaddy = ""
                self.email = ""
                self.payInfo = 0
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
        
        #PAYINFO
        def setPayinfo(self, pay):
                self.payInfo = pay
        def getPayinfo(self):
                return self.payInfo
                
        


        #Controls all of the communication with the database<3
        def register(self,connection):
                username = input("Please enter your Username: ")
                self.setUsrname(username)
                password = getpass.getpass("Please enter your Password: ")
                self.setPass(password)
                Fname = input("Please enter your First name: ")
                Lname = input("Please enter your Last name: ")
                self.setFName(Fname)
                self.setLName(Lname)
                addy =  input("Enter your address: ")
                self.setAddy(addy)
                self.setShpAddy(addy)
                email =  input("Enter your email: ")
                self.setEmail(email)
                namepkg = (self.getUsrname(), self.getPass(), self.getFName(),self.getLName(), self.getAddy(), self.getEmail(), self.getShpAddy())
                cursor = connection.cursor()
                query = ("INSERT INTO customer (Username, Password, Firstname, Lastname, Address, Email, ShippingAddress) VALUES (?,?,?,?,?,?,?)")
                cursor.execute(query,namepkg)
                connection.commit()
        
        def update(self,updatepkg,cursor):
                print("Reviewing the UPDATED information:")
                print(updatepkg)
                review = input("Is the information correct? Y or N ")
                if review == 'Y':
                      query = ("UPDATE customer SET Firstname = ? ,  Lastname =?, Address = ?, Email = ?, ShippingAddress = ? WHERE Username = ?") 
                      cursor.execute(query,updatepkg)

        def editHistory(self,custmr, cursor, connection):
                print("EDITING: ")
                print("1: Shipping Address")
                print("2: Payment Information")
                update = input("Which one do you want to update?")
                if update == "1":
                        shippingadd = input("Please enter your new shipping address:")
                        custmr.setShpAddy(shippingadd)
                        username = custmr.getUsrname()
                        shppkg = (shippingadd, username)
                        print(shippingadd)
                        review = input("Is the information correct? Y or N ")
                        if review == 'Y':
                                query = ("UPDATE customer SET shippingaddress = ? WHERE Username = ?")
                                cursor.execute(query, shppkg )
                                connection.commit()

                elif update == "2":
                        payhis = input("Please enter your new payment information:")
                        custmr.setPayinfo(payhis)
                        username = custmr.getUsrname()
                        paypkg = (payhis, username)
                        print(payhis)
                        review = input("Is the information correct? Y or N ")
                        if review == 'Y':
                                query = ("UPDATE customer SET payinfo = ? WHERE Username = ?")
                                cursor.execute(query, paypkg )
                                connection.commit()
        
        def PersInfo(self):
                Fname = input("Please enter your First name: ")
                Lname = input("Please enter your Last name: ")
                self.setFName(Fname)
                self.setLName(Lname)
                addy =  input("Enter your address: ")
                self.setAddy(addy)
                self.setShpAddy(addy)
                email =  input("Enter your email: ")
                self.setEmail(email)
                namepkg = (self.getAddy(), self.getEmail(), self.getShpAddy())
                return namepkg                
        
        def login(self, cursor):
                while True:
                        username = input("Please enter your Username: ")
                        self.setUsrname(username)
                        password = getpass.getpass("Please enter your Password: ")
                        self.setPass(password)

                        cursor.execute("SELECT * FROM Customer WHERE username = ? AND password = ?", (username, password,))
                        result = cursor.fetchall()
                        cursor.execute('SELECT customerID FROM Customer WHERE username = ? AND password = ?', (username, password,))
                        id = cursor.fetchone()
                        #id = result[5]
                        self.setID(id)
                        if result:
                                print("Accepted")
                                break
                        else:
                                print("Wrong username or password...")
                
                
  