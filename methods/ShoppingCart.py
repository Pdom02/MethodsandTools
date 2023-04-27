import sqlite3
import getpass
import os

sqliteConnection = sqlite3.connect('User_datab.db')


class ShoppingCart:
    def __init__(self):
        self.items = []

    def addCartItem(self,item):
        pid=int(input("Enter ProductId: "))
        print("ProdcutId is: ",pid)
        pname=input("Enter ProductName: ")
        print("ProductName is:",pname)
        pprice=int(input("Enter ProductPrice: "))
        print("ProductPrice is: ",pprice)
        pqty=int(input("Enter ProductQuantity: "))
        print("ProductQuantity is: ",pqty)
        
        con=sqlite3.connect("cart.db")
        c=con.cursor()
        d=c.execute("INSERT INTO product (pId,pName,pPrice,pQty) VALUES (?,?,?,?)",(pid,pname,pprice,pqty))
        con.commit()
        
        if(d):
            print ("Inserted successfull!\n\n")
        else:
            print ("An error occured")

    def removeCartItem(self):
        a=input("Enter ItemID for Deleting")
        if(a):
            con=sqlite3.connect("cart.db")
            c=con.cursor()
            c.execute('DELETE FROM product WHERE pId = ?',(a))
            con.commit()
            c.close()
        
        else:
            print("Please give correct input")

    def viewCart(self):
        print( "Cart Items: ")
        for x in self.items:
            print: x.name ; x.price
            print ("\n")

    def updateQuantity(self):
        b = int(input("What do you want to update the quantity to? "))
        if (b):
            con=sqlite3.connect("cart.db")
            c=con.cursor()
            c.execute('UPDATE product SET pQty= ?',(b))
            con.commit()
            c.close()
        
        else:
            print("Please give correct input")
    
    def totalPrice(self):
        price = 0
        for x in self.items:
            price = price + x.price 
        return price

    def checkout(self):
        for item in cart:
            con=sqlite3.connect("cart.db")
            c=con.cursor()
            #c.execute('DELETE FROM product WHERE )
            con.commit()
            c.close()
        


def main():

    cart = {}
    print ("Welcome to your cart!")

    while(1):
        print ("\nPlease choose an option:")
        print ("\t1. Add Item")
        print ("\t2. Remove Item")
        #print ("\t3. Update quantity") 
        print ("\t3. View Cart")
        print ("\t4. Compute Total Price")
        print ("\t5. Checkout")

        select = input("\nType the number of the option you want: ")

        if select == '1':
            item = input("What Item would you like to add?  ")
            cart.addCartItem(item)

        if select == '2':
            if cart: 
                remove = input("What Item would you like to remove?  ")
                cart.removeCartItem(remove)
            else:
                print("\n\tThere are no items in your cart.\n")

        if select == '3':
            if cart:
                print("This is what is in your cart:")
                cart.viewCart()
            else:
                print("\n\tThere are no items in your cart.\n")

        if select == '4':
            total = 0
            for item in cart:
                total += cart[item]
            print(f" ${total}")

        if select == '5':
            cart.checkout()
            print("Have a great day and come back soon!" )
            break

main()
