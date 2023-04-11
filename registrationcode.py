
import re
import mysql.connector

class xyz:

    def __init__(self):
        self.email = ""
        self.password = ""
        self.localhost = ""
        self.username = ""
        self.password = ""
        self.database_name = ""
        self.table_name = ""

    def get_email(self):

        while True:
            email = input("Enter your email :  ")
            if re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email):
                self.email = email
                break
            else:
                print("please enter valid email")


    def get_password(self):

        while True:
            password = input("Enter your password: ")
            if re.match("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@%$#^&*/!_])[a-zA-Z\d@%$#^&*/!_]{8,12}",password):
                self.password=password
                break

            elif len(password) < 8:

                print("enter at least 8 characters")

            else:
                print("please enter valid password")

    def register(self):

        mydb = mysql.connector.connect(host=self.localhost, user=self.username, password=self.password, database=self.database_name)
        cur = mydb.cursor()


        self.get_email()
        self.get_password()
        cur.execute("INSERT INTO "+self.table_name+" (email, password ) VALUES (%s, %s)", (self.email, self.password))

        mydb.commit()
        print("Registration successful!")

    def login(self):
        mydb = mysql.connector.connect(host=self.localhost, user=self.username, password=self.password, database=self.database_name)
        cur = mydb.cursor()
        while True:
            email = input("Enter your email: ")

            cur.execute("SELECT email, password FROM "+self.table_name+" WHERE email=%s", (email,))
            row = cur.fetchone()

            if row is not None:
                while True:
                    password = input("Enter your password: ")

                    if row[1] == password:
                        print("Login successful!")
                        break
                    else:
                        print("Incorrect password. Login unsuccessful.")
                break
            else:
                print("Email does not exist. Login unsuccessful.")

obj=xyz()
obj.register()
obj.login()

























