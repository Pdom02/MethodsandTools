import sqlite3
import getpass
import os

def clear():
    os.system('clear')


def main_loop():
    connection = sqlite3.connect("buyerschoice.db")
    cursor = connection.cursor()
    # print("Welcome to buyers choice!\n")
    # print("1. Login")
    # print("2. Register")
    # check1 = input("Type one of the numbers: ")
    # quit = 0
    while(1):
        print("Welcome to buyers choice!\n")
        print("1. Login")
        print("2. Register")
        check1 = input("Type one of the numbers: ")
        quit = 0
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
                    print("Current Username: " + username)
                    print("Password: ********")
                    print(f"Address: {result2!r}")
                    print(f"Email Address: {result!r} ")
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
