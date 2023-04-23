import sqlite3
import getpass
import os

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
                                    payinfo	text
                                );"""
    sql_create_item_table = """ CREATE TABLE IF NOT EXISTS listing (
                                itemName text,
	                            itemID	integer PRIMARY KEY,
	                            itemDesc text,
	                            itemPrice numeric,
	                            itemStock integer,
	                            itemCategory integer
                            );"""
    
    sql_create_cart_table = """ CREATE TABLE IF NOT EXISTS cart (
                                    cartID integer PRIMARY KEY,
                                    itemID integer listing,
                                    quantity integer,
                                    FOREIGN KEY (itemID) REFERENCES listing(itemID)
                            );"""
    
    connection = sqlite3.connect("buyerschoice.db")

    if connection is not None:
        #creates customer table
        create_table(connection, sql_create_customer_table)
        #creates listing table
        create_table(connection, sql_create_item_table)
        #creates cart table
        create_table(connection, sql_create_cart_table)

def main_loop():
    setup_db()
    connection = sqlite3.connect("buyerschoice.db")
    cursor = connection.cursor()
    quit = 0
    while(1):
        print("Welcome to buyers choice!\n")
        print("1. Login")
        print("2. Register")
        check1 = input("Type one of the numbers: ")
        if check1 == "1":
            clear()
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            try:
                cursor.execute("SELECT * FROM Customer WHERE username = ? AND password = ?", (username, password))
            except:
                print("Wrong username or password...")
            clear()
            while(quit != 1):
                print("Welcome "  + username)
                print("1. Update Profile content")
                print("2, Add Listing")
                print("3. Search Listings")
                print("4. Logout")
                check2 = input("Type one of the numbers: ")
                if check2 == "1":
                    email = cursor.execute("SELECT email FROM Customer WHERE username = ? AND password = ?", (username, password))
                    result = email.fetchone()
                    address = cursor.execute("SELECT address FROM Customer WHERE username = ? AND password = ?", (username, password))
                    result2 = address.fetchone()
                    payinfo = cursor.execute("SELECT payinfo FROM Customer WHERE username = ? AND password = ?", (username, password))
                    result3 = payinfo.fetchone()
                    print("Current Username: " + username)
                    print("Password: ********")
                    print(f"Address: {result2!r}")
                    print(f"Email Address: {result!r} ")
                    print(f"Payment Information: {result3!r} ")
                if check2 == "2":
                    itemName = input("Item Name: ")
                    itemDesc = input("Itme Description: ")
                    itemPrice = float(input("Price: $"))
                    itemStock = int(input("Stock: "))
                    itemCategory = input("Category: ")
                    datapkg = (itemName, itemDesc, itemPrice, itemStock, itemCategory)
                    cursor.execute("INSERT INTO Listings(itemName, itemDesc, itemPrice, itemStock, itemCategory) VALUES(?, ?, ?, ?, ?)", datapkg)
                    connection.commit()
                if check2 == "3":
                    listingname = input("Search for an item listing: ")
                    cursor.execute("SELECT * FROM Listings WHERE itemName = ?", (listingname, ))
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
                    break

        elif check1 == "2":
            print("Registration")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            firstname = input("First name: ")
            lastname = input("Last name: ")
            address = input("Address: ")
            email = input("Email: ")
            datapkg = (firstname, lastname, username, password, address, email)
            cursor.execute("INSERT INTO Customer(firstname, lastname, username, password, address, email) VALUES(?, ?, ?, ?, ?, ?)", datapkg)
            connection.commit()
            check1 = "1"






main_loop()
