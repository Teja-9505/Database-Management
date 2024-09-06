import mysql.connector as mysql

cn = mysql.connect(user='root', password='root')

def CreateDatabase():
    c = cn.cursor()
    name = input("Enter The Name of the database : ")
    try:
        c.execute(f"create database {name}")
        cn.commit()
        print("Database created......")
    except mysql.Error as e:
        print(f"Error: {e}")

def DeleteDatabase():
    c = cn.cursor()
    name = input("Enter the database name you want to delete : ")
    try:
        c.execute(f"drop database {name}")
        cn.commit()
        print("Database deleted")
    except mysql.Error as e:
        print(f"Error : {e}")

def CreateTable():
    c = cn.cursor()
    dname = input("Enter the database name where you want to create table : ")
    tname = input("Enter the table name : ")
    try:
        c.execute(f"use {dname}")
        c.execute(f"create table `{tname}`(ID integer primary key,ename varchar(20),job varchar(20),salary float(10,2))")
        cn.commit()
        print("Table created......")
    except mysql.Error as e:
        print(f"Error : {e}")



def DeleteTable():
    c = cn.cursor()
    dname = input("Enter the database name that table is in : ")
    tname = input("Enter the table name : ")
    try:
        c.execute(f"use {dname}")
        c.execute(f'drop table `{tname}`')
        cn.commit()
        print("Table deleted.....")
    except mysql.Error as e:
        print(f'Error : {e}')


def Insertdata():
    c = cn.cursor()
    dname = input("Enter the database name the table is in : ")
    tname = input("Enter table name : ")
    while True:
        empid = int(input("Enter the ID of Employee : "))
        ename = input("Enter the name of the employee : ")
        job = input("Enter the employee Job : ")
        sal = float(input("Enter the salary of the employee : "))
        try:
            c.execute(f"use {dname}")
            c.execute(f'insert into `{tname}` values(%s,%s,%s,%s)',params=(empid,ename,job,sal))
            cn.commit()
            print("Data inserted.......")
        except mysql.Error as e:
            print(f"Error : {e}")
        except ValueError:
            print("Enter data correctly")
        ans = input("Do you what to add another employee data(y/n) : ")
        if ans == 'n':
            break


def DeletebyID():
    c = cn.cursor()
    dname = input("Enter database name that table is in : ")
    tname = input("Enter table name : ")
    while True:
        id = int(input("Enter the id of employee to delete : "))
        try:
            c.execute(f"use {dname}")
            c.execute(f'delete from `{tname}` where ID = {id}')
            cn.commit()
            if c.rowcount == 0:
                print("ID does not exist")
            else:
                print("Data Deleted....")
        except mysql.Error as e:
            print(f"Error : {e}")
        ans = input("Do you delete another employee data?(y/n) : ")
        if ans == 'n':
            break


def UpdatebyID():
    c = cn.cursor()
    dname = input("Enter database name that table is in : ")
    tname = input("Enter the table name : ")
    while True:
        try:
            id = int(input("Enter the Employee ID : "))
            sal = float(input("Enter the Incremented Salary : "))
            c.execute(f"use {dname}")
            c.execute(f'update `{tname}` set salary = salary + {sal} where ID = {id}')
            cn.commit()
            if c.rowcount == 0:
               print("ID does not exist....")
            else:
                print("Data Updated.....")
            ans = input("Do you want to update another employee salary?(y/n) : ")
            if ans =='n':
                break
        except mysql.Error as e:
            print(f'Error : {e}')



def Displaydata():
    c = cn.cursor()
    dname = input("Enter Database name where that table is stored : ")
    tname = input("Enter the table name : ")
    try:
        c.execute(f'use {dname}')
        c.execute(f'select * from `{tname}`')
        str = list(c.fetchall())
        for s in str:
            print(f'{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}')
    except mysql.Error as e:
        print(f"Error : {e}")


while True:
    try:
        print("\n")
        print("**************************************")
        print("1. Create Database")
        print("2. Delete database")
        print("3. Create Table")
        print("4. Delete Table")
        print("5. Insert data into table")
        print("6. Delete data by ID")
        print("7. Update table data by ID")
        print("8. Display data of the table")
        print("9. Exit")
        print("**************************************")
        print("\n")
        opt = int(input("Enter Your option : "))
        match opt:
            case 1:
                CreateDatabase()
            case 2:
                DeleteDatabase()
            case 3:
                CreateTable()
            case 4:
                DeleteTable()
            case 5:
                Insertdata()
            case 6:
                DeletebyID()
            case 7:
                UpdatebyID()
            case 8:
                Displaydata()
            case 9:
                break
            case _:
                print("Enter integer between 1-9")
    except Exception as e:
        print(f"Error : {e}")
