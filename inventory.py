import os
import mysql.connector as sqltor
import datetime
now=datetime.datetime.now()

def product_mgmt():
    while True:
        print("\t\t\t 1.Add New Product")
        print("\t\t\t 2.List Product")
        print("\t\t\t 3.Update Product")
        print("\t\t\t 4.Delete product")
        print("\t\t\t 5.Back(Main Menu)")
        p=int(input("\t\t\t\t\t Enter Your Choice:"))
        if p==1:
            add_product()
        if p==2:
            search_product()
        if p==3:
            update_product()
        if p==4:
            delete_product()
        if p==5:
            break

def purchase_mgmt():
    while True:
        print("\t\t\t 1.Add Order")
        print("\t\t\t 2.List Order")
        print("\t\t\t 3.Back(Main Menu)")
        o=int(input("\t\t\t\tEnter your choice:"))
        if o==1:
            add_order()
        if o==2:
           list_order()
        if o==3:
            break

def sales_mgmt():
    while True:
        print("\t\t\t 1.Sale Items")
        print("\t\t\t 2.List Sales")
        print("\t\t\t 3.Back(Main Menu)")
        s=int(input("\t\t\t\t Enter Your Choice:"))
        if s==1:
            sale_product()
        if s==2:
            list_sale()
        if s==3:
            break

def user_mgmt():
    while True:
        print("\t\t\t 1.Add user")
        print("\t\t\t 2.List user")
        print("\t\t\t 3.Back(Main Menu)")
        u=int(input("\t\t\t\t Enter Your Choice:"))
        if u==1:
            add_user()
        if u==2:
            list_user()
        if u==3:
            break

def create_database():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")
    
    mycursor=mydb.cursor()
    print("Creating PRODUCT table")
    sql="CREATE TABLE if not exists product(pcode int(4) PRIMARY KEY,pname char(30) NOT NULL,price float(8,2),pqty int(4),pcat char(30));"
    mycursor.execute(sql)
    print("Product table created")
    
    '''print("CREATING ORDER table")
    sql="CREATE TABLE if not exists order(orderid int(4) Primary key,orderdate DATE,pcode char(30)NOT NULL,pprice float(8,2),pqty int(4),supplier char(50),pcat char(30));"
    mycursor.execute(sql)
    print("ORDER table created")'''
    
    print("Creating SALES table")
    sql="CREATE TABLE if not exists sales(salesid int(4),salesdate DATE,pcode char(30) references product(pcode),pprice float(8,2),pqty int(4),Total double(8,2));"
    mycursor.execute(sql)
    print("SALES table created")
    
    sql="CREATE TABLE if not exists user(uid char(6) PRIMARY KEY,uname char(30) NOT NULL,UPWD CHAR(30));"
    mycursor.execute(sql)
    print("USER table created")

    print("CREATING ORDER table")
    sql="CREATE TABLE if not exists orders(orderid int(4) Primary key,orderdate DATE,pcode char(30)NOT NULL,pprice float(8,2),pqty int(4),supplier char(50),pcat char(30));"
    mycursor.execute(sql)
    print("ORDER table created")

def list_database():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    sql="show tables;"
    
    mycursor.execute(sql)
    for i in mycursor:
        print(i)

def add_order():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    now=datetime.datetime.now()
    sql="INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat)values(%s,%s,%s,%s,%s,%s,%s)"
    code=int(input("\tEnter product code :_ "))
    oid=now.year+now.month+now.day+now.hour+now.minute+now.second
    qty=int(input(("\tEnter product quantity :_ ")))
    price=float(input("\tEnter Product unit price :_ "))
    cat=input("\tEnter product category :_ ")
    supplier=input("\tEnter Supplier details :_ ")
    val=(oid,now,code,price,qty,supplier,cat)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record(s) added!");

def list_order():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")
    
    mycursor=mydb.cursor()
    sql="SELECT * from orders"
    
    mycursor.execute(sql)
    print("\t\t\t\t\tORDER DETAILS")
    print("-"*130)
    print("OrderID" "\t    Date" "\t        Product Code" "\tPrice" "\tQuantity" "\t  Supplier"  "\t\tCategory")
    print("-"*130)
    for i in mycursor:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\t",i[6])
    print("-"*130)

def db_mgmt():
    while True:
        print("\t\t\t 1.Database creation")
        print("\t\t\t 2.List Database")
        print("\t\t\t 3.Back(Main Menu)")
        p=int(input("\t\t Enter Your Choice :_ "))
        if p==1:
            create_database()
        if p==2:
            list_database()
        if p==3:
            break

def add_product():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    sql="INSERT INTO product(pcode,pname,price,pqty,pcat)values(%s,%s,%s,%s,%s)"
    code=int(input("\t Enter product code :_ "))
    search="SELECT count(*) FROM product WHERE pcode=%s;"
    val=(code,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt=x[0]
    if cnt==0:
        name=input("\t\t Enter product name(only 9 characters) :_ ")        
        qty=int(input("\t\t Enter product quantity :_ "))
        price=float(input("\t\t Enter product unit price :_ "))
        cat=input("\t\t Enter Product category :_ ")
        val=(code,name,price,qty,cat)        
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,"record(s) added!");
    else:
        print("\t\t Product already exists!")

def update_product():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    code=int(input("\tEnter the product code :_ "))
    qty=int(input("\tEnter the quantity :_ "))
    sql="UPDATE product SET pqty=pqty+%s where pcode=%s;"
    val=(qty,code)
           
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t\t Product details updated!")

def delete_product():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    code=int(input("\tEnter the product code :_ "))
    sql="DELETE FROM product WHERE pcode=%s;"
    val=(code,)

    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record(s) deleted!");

def search_product():
    while True:
        print("\t\t\t 1.List all products")
        print("\t\t\t 2.List all products code wise")
        print("\t\t\t 3.List all products category wise")
        print("\t\t\t 4.Back(Main Menu)")
        s=int(input("\t\t Enter Your Choice :_ "))
        if s==1:
            list_product()
        if s==2:
            code=int(input("\tEnter product code :_ "))
            list_prcode(code)
        if s==3:
            cat=input("\tEnter product category :_ ")
            list_prcat(cat)
        if s==4:
            break

def list_product():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    sql="SELECT*from product"

    mycursor.execute(sql)
    print("\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*80)
    print("\t\t CODE""\t NAME""\t PRICE""\t QUANTITY   ""\t CATEGORY")
    print("\t\t","-"*80)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4])
    print("\t\t","-"*80)

def list_prcode(code):
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    sql="SELECT*from product WHERE pcode=%s"
    val=(code,)

    mycursor.execute(sql,val)
    print("\t\t","-"*100)
    print("\t\t CODE" "\t  NAME" "\t  PRICE" "\t  QUANTITY" "\t  CATEGORY")
    print("\t\t","-"*100)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4])
    print("\t\t","-"*100)

def sale_product():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    pcode=input("\tEnter product code :_ ")
    sql="SELECT count(*) from product WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(sql,val)
    
    for x in mycursor:
        cnt=x[0]
    if cnt!=0:
        sql="SELECT * from product where pcode=%s;"
        val = (pcode,)
        mycursor.execute(sql,val)
        for x in mycursor:
            print(x)
            price=int(x[2])
            pqty=int(x[3])
            qty=int(input("\tEnter no of quantity:"))
            if qty <= pqty:
                total = qty*price
                print("Collect rs.",total)
                sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
                val=(int(cnt)+1,datetime.datetime.now(),pcode,price,qty,total)
                mycursor.execute(sql,val)
                sql="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
                val=(qty,pcode)
                mycursor.execute(sql,val)
                mydb.commit()
            else:
                print("Quantity not available")
    else:
        print("Product not available")

def list_sale():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    sql="SELECT*FROM sales"
    mycursor.execute(sql)
    print("\t\t\t SALES DETAILS")
    print("-"*120)
    print("Sales ID" "\t\tDate" "\tProduct_Code" "\tPrice" "\tQuantity" "\t\tTotal")
    print("-"*120)
    for x in mycursor:
        print(x[0],"\t",x[1],"\t",x[2],"\t\t",x[3],"\t",x[4],"\t\t",x[5])
    print("-"*120)

def list_prcat(cat):
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    print(cat)
    sql="SELECT*from product WHERE pcat=%s"
    val=(cat,)
    mycursor.execute(sql,val)
    clrscr()
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*90)
    print("\t\t CODE" "\t  NAME" "\t  PRICE" "\t  QUANTITY ""\t  CATEGORY")
    print("\t\t","-"*90)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4])
    print("\t\t","-"*90)

def add_user():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    uid=input("\tEnter ID :_ ")
    name=input("\tEnter Name :_ ")
    password=input("\tEnter Password :_ ")
    sql="INSERT INTO user values(%s,%s,%s);"
    val=(uid,name,password)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"user created")

def list_user():
    mydb=sqltor.connect(host="localhost",user="root",password="root1234",database="stock")

    mycursor=mydb.cursor()
    sql="SELECT uid,uname,upwd from user"
    mycursor.execute(sql)
    clrscr()
    print("\t\t\t\t USER DETAILS")
    print("\t\t","-"*50)
    print("\t\t UID \t Name \t Password ")
    print("\t\t","-"*50)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2])
    print("\t\t","-"*50)

def clrscr():
    print("\n"*5)

while True:
    clrscr()
    print("\t\t\t INVENTORY MANAGEMENT")
    print("\t\t\t *******************")
    print("\t\t 1.PRODUCT MANAGEMENT")
    print("\t\t 2.PURCHASE MANAGEMENT")
    print("\t\t 3.SALES MANAGEMENT")
    print("\t\t 4.USER MANAGEMENT")
    print("\t\t 5.DATABASE SETUP")
    print("\t\t 6.EXIT\n")
    n=int(input("Enter your choice :_ "))
    if n==1:
        product_mgmt()
    if n==2:
        os.system("cls")
        purchase_mgmt()
    if n==3:
        sales_mgmt()
    if n==4:
        user_mgmt()
    if n==5:
        db_mgmt()
    if n==6:
        print(" THANK YOU FOR SELECTING INVENTORY MANAGEMENT SYSTEM. ")
        print("\t \t HAVE A GOOD DAY.")
        break
