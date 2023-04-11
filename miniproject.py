import re
import mysql.connector

class user:
    def __init__(self):
        self.name=""
        self.contact=""
        self.localhost = ""
        self.username = ""
        self.password = ""
        self.database_name = ""
        self.table_name = ""
        self.mydb = mysql.connector.connect(host=self.localhost, user=self.username, password=self.password,database=self.database_name)

    def register(self):

        while True:
            name=input("Enter yout Name   ")
            if re.match("[A-Za-z]{2,25}\s[A-Za-z]{2,25}", name):
                self.name=name
                while True:
                    contact = input("Enter your contact number ")
                    if re.match("[0-9]{10}", contact):
                        self.contact=contact
                        print("Registered successfully")
                        break
                    else:
                        print("Please enter valid contact number ")
                break
            else:
                print("Please enter appropriate name")


        cur = self.mydb.cursor()

        cur.execute("INSERT INTO "+self.table_name+" (name, contact ) VALUES (%s, %s)", (self.name, self.contact))

        self.mydb.commit()
        print(" data updated")

    def read(self):
        mydb = mysql.connector.connect(host=self.localhost, user=self.username, password=self.password,
                                       database=self.database_name)
        cur = mydb.cursor()

        cur.execute("SELECT * FROM "+self.table_name+" "  )

        myresult = cur.fetchall()

        for x in myresult:
            print(x)

    def get_detailes(self):
        while True:
            print('Search by name:')

            name = input()
            cur = self.mydb.cursor()
            cur.execute("SELECT name, contact FROM "+self.table_name+" WHERE name=%s", (name,))
            row = cur.fetchone()
            if row is not None:
                    for i in row:
                        print(i)
                    break
            else:
                print("We don't have member with this name",name)


    def delete(self):

            print('Search by id:')
            id = input()
            cur = self.mydb.cursor()
            row=cur.execute("DELETE FROM "+self.table_name+" WHERE id=%s", (id,))
            self.mydb.commit()
            if row:
                print(cur.rowcount, "record deleted.")
            else:
                print("we don't have this data")

obj=user()
obj.register()
obj.read()
obj.delete()










