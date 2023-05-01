''''  Student Marksheet Solution

Allow to manage student marksheet solution with help of script, command line options and choise to execute each operation.

Cover below operations

- allow to add student details. like name email, rollno, mobile, male/female, insert/update/delete/search/read operation

- allwo to add subject details, subject, minimum, maximum. (min, max use for validation purpose for accurate data entry)

- Allow to add marksheet details for a student, where we can select student via roll number and can add all subject related user's obtained marks

- Print for single student marksheete

- print how many studetn pass or failed

- Print city wise students and their total marks

    '''


import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database=" ")
cur=mydb.cursor()

class Student:


    def add_student(self):
        Name = input("Enter student name: ")
        Email = input("Enter student email: ")
        Mobile = input("Enter student mobile: ")
        City=input("Enter city: ")
        # Insert student details into database
        cur.execute("INSERT INTO student (name, email, mobile, city ) values (%s,%s,%s,%s)",(Name,Email,Mobile,City))
        mydb.commit()
        print(cur.rowcount, "record inserted.")



    def add_marks(self):
        S_name = input("Enter the name of subject:  ")
        marks = int(input("Enter marks obtained by student: "))
        roll_no = int(input("Enter roll no: "))

        cur.execute("SELECT * FROM student WHERE rollno=%s", (roll_no,))
        myresult = cur.fetchone()
        if myresult:
            cur.execute("INSERT INTO subject (s_name,rollno,obtained_marks) values (%s,%s,%s)", (S_name,roll_no,marks))
            mydb.commit()
            print("Marks added successfully!")
        else:
            print("Roll no not found!")
    def marksheet(self):
        roll_no=input("search by rollno:   ")
        cur.execute("SELECT subject.rollno,name,s_name,minimum,maximum,obtained_marks FROM subject JOIN student ON subject.rollno=student.rollno WHERE student.rollno=%s",(roll_no,))
        myresult=cur.fetchall()
        for x in myresult:
            print(x)
    def result(self):
        roll_no=input("search by rollno:   ")
        cur.execute("SELECT *  FROM subject WHERE rollno=%s ",(roll_no,))
        myresult=cur.fetchall()
        total=0
        for i in myresult:
            total+=i[5]
            if i[5]<35:
                print(f"student with rollno {roll_no} has failed the exam")
                break
            else:
                print(f"student with rollno {roll_no} has passed the exam with total marks {total}")
    def citywisetotal(self):
        cur.execute("SELECT student.rollno, student.city, SUM(subject.obtained_marks) FROM student JOIN subject ON student.rollno = subject.rollno GROUP BY  student.city")
        myresult=cur.fetchall()
        for i in myresult:
            print(i)

stud=Student()

if __name__== "__main__":
    while True:
        print(''' 
        
        1. add_student
        2. add_marks
        3. marksheet
        4. result
        5. citywisetotal
    
        ''')

        choice=input("Enter your choice:  ")

        if choice=="1":
            stud.add_student()
        if choice=="2":
            stud.add_marks()
        if choice=="3":
            stud.marksheet()
        if choice=="4":
            stud.result()
        if choice=="5":
            stud.citywisetotal()


        option=input("press c to continue q to quit")
        if option=="c":
            continue
        if option=="q":
            break























