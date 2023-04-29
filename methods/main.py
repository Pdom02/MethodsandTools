import sqlite3
import getpass
import os
from user_class import User
from Item_class import Item
from cart_class import ShoppingCart
from store_class import Store

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def create_table(conn, create_table_sql):
    
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except RuntimeError as e:
        print(e)

def setup_db():
    database = r"C:\\Users\\Phillip Dominguez\\Desktop\\methods_tools\\MethodsandTools\\methods\\buyerschoice.db"

    sql_create_customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                                    firstname text,
                                    lastname text,
                                    username text,
                                    password text,
                                    address	text,
                                    customerID integer PRIMARY KEY,
                                    email text,
                                    payHis integer,
                                    orderHis integer,
                                    order_info integer,
                                    payinfo	text,
                                    shippingaddress text
                                );"""
    sql_create_item_table = """ CREATE TABLE IF NOT EXISTS items (
                                itemName text,
	                            itemID	integer PRIMARY KEY,
	                            itemDesc text,
	                            itemPrice numeric,
	                            itemStock integer,
	                            itemCategory integer
                            );"""
    
    sql_create_cart_table = """ CREATE TABLE IF NOT EXISTS cart (
                                    cartID integer PRIMARY KEY,
                                    itemName TEXT,
                                    quantity integer
                                    customerID integer,
                                    FOREIGN KEY (customerID) REFERENCES customer (customerID)
                            );"""
    
    sql_create_orders_table = """ CREATE TABLE IF NOT EXISTS orders (
                                    orderID PRIMARY KEY,
                                    itemName TEXT,
                                    itemStock INTEGER,
                                    customerID INTEGER,
                                    FOREIGN KEY (customerID) REFERENCES customer (customerID)
                            );"""
    
    connection = sqlite3.connect("buyerschoice.db")

    if connection is not None:
        #creates customer table
        create_table(connection, sql_create_customer_table)
        #creates listing table
        create_table(connection, sql_create_item_table)
        #creates cart table
        create_table(connection, sql_create_cart_table)
        #creates orders table
        create_table(connection, sql_create_orders_table)

def main_loop():
    setup_db()
    connection = sqlite3.connect("buyerschoice.db")
    cursor = connection.cursor()
    adminID = "admin"
    adminPass = "123admin"
    adminguy = Store(adminID, adminPass)
    fella = User(connection)
    cart = ShoppingCart(connection)

    quit = 0
    while(1):
        print("Welcome to buyers choice!\n")
        print("1. Login")
        print("2. Register")
        print("3. Admin Portal")
        print("4. Exit")
        check1 = input("Type one of the numbers: ")
        if check1 == "1":
            clear()
            fella.login(cursor)
            
            while(quit != 1):
                print("Welcome "  + fella.getUsrname())
                print("1. Update Profile content")
                print("2. Show listings")
                print("3. Search Listings")
                print("4. View Cart")
                print("5. Order History")
                print("6. Checkout")
                print("7. Logout")
                check2 = input("Type one of the numbers: ")
                if check2 == "1":
                    email = cursor.execute("SELECT email FROM Customer WHERE username = ? AND password = ?", (fella.getUsrname(), fella.getPass()))
                    result = email.fetchone()
                    address = cursor.execute("SELECT address FROM Customer WHERE username = ? AND password = ?", (fella.getUsrname(), fella.getPass()))
                    result2 = address.fetchone()
                    payinfo = cursor.execute("SELECT payinfo FROM Customer WHERE username = ? AND password = ?", (fella.getUsrname(), fella.getPass()))
                    result3 = payinfo.fetchone()
                    print("Current Username: " + fella.getUsrname())
                    print("Password: ********")
                    print(f"Address: {result2!r}")
                    print(f"Email Address: {result!r} ")
                    print(f"Payment Information: {result3!r} ")
                if check2 == "2":
                    cursor.execute("SELECT * FROM Listings")
                    rows = cursor.fetchall()
                    if len(rows) == 0:
                        print("No listings found.")
                    else:
                        for row in rows:
                            print()
                            name = print("Name:", row[0])
                            print("Description:", row[2])
                            print("Price: ${:.2f}".format(row[3]))
                            print("Stock:", row[4])
                            print("Category:", row[5])
                            print()
                    check4 = input("Type the name of the item you'd like to purchase: ")
                    check5 = input("Type item quanitity: ")
                    for row in rows:
                        if check4 == row[0]:
                            new_item = Item(row[0], row[1] ,row[2], row[3], check5, row[5])
                            cart.addItem(new_item.getitemName(), new_item.getitemID(), new_item.getitemDesc(), new_item.getitemPrice(), new_item.getitemStock(), new_item.getitemCategory())
                        else:
                            print("Please enter a proper item name")
                            continue
                if check2 == "3":
                    listingname = input("Search for an item listing: ")
                    cursor.execute("SELECT * FROM Listings WHERE itemName = ?", (listingname))
                    rows = cursor.fetchall()

                    if len(rows) == 0:
                        print("No listings found.")
                    else:
                        for row in rows:
                            print()
                            print("Name:", row[0])
                            print("Description:", row[2])
                            print("Price: ${:.2f}".format(row[3]))
                            print("Stock:", row[4])
                            print("Category:", row[5])
                            print()
                if check2 == "4":
                    cart.viewCart()
                if check2 == "7":
                    break
                    

        elif check1 == "2":
            fella.register(connection)
        elif check1 == "3":
            username = input("Username: ")
            password = getpass.getpass("Passowrd: ")
            if (username == adminguy.getadminID()) & (password == adminguy.getadminPass()):
                while(1):
                    clear()
                    print("Admin Panel")
                    print("1. View Listings")
                    print("2. View Accounts")
                    print("3. Logout")
                    admin_choice = input("Type the number of the option you want to select: ")
                    if admin_choice == '1':
                        cursor.execute("SELECT * FROM Listings")
                        rows = cursor.fetchall()
                        if len(rows) == 0:
                            print("No listings found.")
                            goback = input("Type 'b' to go back: ")
                            if goback == 'b':
                                continue
                        else:
                            for row in rows:
                                print()
                                print("Name:", row[0])
                                print("ID: ", row[1])
                                print("Description:", row[2])
                                print("Price: ${:.2f}".format(row[3]))
                                print("Stock:", row[4])
                                print("Category:", row[5])
                                print()
                        rmv_choice = input("Type the itemID that you wish to remove, or type 'b' to go back: ")
                        if rmv_choice == 'b':
                            continue
                        else:
                            adminguy.removeListing(connection, cursor, rmv_choice)
                    if admin_choice == '2':
                        cursor.execute("SELECT * FROM Customer")
                        rows = cursor.fetchall()
                        if len(rows) == 0:
                            print("No customers in DB")
                            goback = input("Type 'b' to go back: ")
                            if goback == 'b':
                                continue
                        else:
                            for row in rows:
                                print()
                                print("Username: ", row[2])
                                print("Full name: ", row[0], row[1])
                                print("ID Num: ", row[5])
                                print()
                            customer_rmv = input("Type the ID Num for the account you wish to remove, or type 'b' to go back: ")
                            if customer_rmv == 'b':
                                continue
                            else:
                                adminguy.removeAccount(connection, cursor, customer_rmv)
                    if admin_choice == '3':
                        break
                    
            else:
                print("Invalid credentials...")
                continue

        elif check1 == "4":
            connection.close()
            exit()





main_loop()