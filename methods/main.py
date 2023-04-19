import sqlite3
import getpass
import os

def clear():
    os.system('cls')


def main_loop():
    connection = sqlite3.connect("buyerschoice.db")
    cursor = connection.cursor()
    print("Welcome to buyers choice!\n")
    print("1. Login")
    print("2. Register")
    check1 = input("Type one of the numbers: ")
    quit = 0
    while(1):
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
                print("2. Search Listings")
                print("3. Logout")
                check2 = input("Type one of the numbers: ")
                if check2 == "1":
                    email = cursor.execute("SELECT email FROM Customer WHERE username = ? AND password = ?", (username, password))
                    result = email.fetchone()
                    address = cursor.execute("SELECT address FROM Customer WHERE username = ? AND password = ?", (username, password))
                    result2 = address.fetchone()
                    print("Current Username: " + username)
                    print("Password: ********")
                    print(f"Adress: {result2!r}")
                    print(f"Email Address: {result!r} ")
                if check2 == "3":
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
