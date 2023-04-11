import datetime
import mysql.connector
class shop:
    def __init__(self):
        self.shopname=shop
        self.localhost = ""
        self.username = ""
        self.password = ""
        self.database_name = ""
        self.table_name = ""
        self.table_name2= ""
        self.table_name3= ""
        print("welcome to our shop")
    def show(self):
        print("choose the products you want to buy")
        self.mydb = mysql.connector.connect(host=self.localhost, user=self.username, password=self.password,database=self.database_name)

        cursor = self.mydb.cursor()

        cursor.execute("SELECT p_id, p_name,selling_price FROM "+self.table_name+"")

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)

    def get_product(self):

        products = []
        quantities = []
        itemtotals=[]
        total=0

        while True:
            p_name=input("Enter the product you want to buy  ")
            quantity1=int(input("Enter the quantity of product you want to buy  "))
            cursor = self.mydb.cursor()
            cursor.execute("SELECT p_id, p_name, selling_price, p_quantity FROM "+self.table_name+" WHERE p_name = %s", (p_name,))
            myresult = cursor.fetchone()

            if myresult is None:
                print("Invalid product name. Please try again.")
                continue

            p_id,p_name, selling_price, p_quantity = myresult

            if p_quantity < quantity1:
                print(f"Sorry, we have only {p_quantity} units of {p_name} available in stock.")

            products.append(p_name)
            quantities.append(quantity1)
            itemtotal = selling_price * quantity1
            itemtotals.append(itemtotal)


            print("Enter c to continue or Enter q to quite ")
            choice1=input()
            if choice1=='c':
                continue
            if choice1=='q':
                break
        if len(products) == 0:
            return

        name=input("Enter your name  ")
        mobile=input("Enter your contact number  ")
        address=input("Enter your address   ")
        cursor = self.mydb.cursor()
        cursor.execute("INSERT INTO "+self.table_name2+" (c_name,c_mobile,c_address ) VALUES (%s, %s,%s)", (name,mobile,address))
        self.mydb.commit()
        c_id = cursor.lastrowid

        for i in range(len(products)):
            p_name = products[i]
            quantity1 = quantities[i]
            itemtotal=itemtotals[i]
            cursor.execute("SELECT p_id, p_name, selling_price, p_quantity FROM "+self.table_name+" WHERE p_name = %s", (p_name,))
            myresult = cursor.fetchone()

            p_id, p_name, selling_price, p_quantity = myresult
            updated_quantity=p_quantity-quantity1
            cursor.execute("UPDATE "+self.table_name+" SET p_quantity = %s WHERE p_name = %s", (updated_quantity, p_name))
            self.mydb.commit()
            print(f"total per items is {itemtotal}")
            total = sum(itemtotals)
            print(f"Thankyou for shoping.Your total is {total}")
            date=datetime.date.today()
            cursor.execute("INSERT INTO "+self.table_name3+" (p_id, c_id,total,date) VALUES (%s, %s, %s,%s)", (p_id, c_id,total,date))
            self.mydb.commit()


obj=shop()
obj.show()
obj.get_product()








