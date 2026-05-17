#IMPLEMENTING CURD OPERATION
'''
#DISPLAY
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    database="userlogin",
    user="root",
    password="pass@33")
cursor = conn.cursor()
query = ("select * from userdetails")
cursor.execute(query)
result = cursor.fetchall()
for r in result:
    print(r)
print("ook")

#INSERTING
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    database="userlogin",
    user="root",
    password="pass@33")
cursor = conn.cursor()
userid = input("enter your userid: ")
username=input("enter your user name: ")
userpass = input("enter your password: ")
query = "insert into userdetails values (%s,%s,%s);"
value = (userid,username,userpass)
cursor.execute(query,value)
conn.commit()
conn.close()
print("ok")

#UPDATE
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    database  = "userlogin",
    user = "root",
    password = "pass@33")
cursor = conn.cursor()
username = input ("Enter your username to be updated: ")
userpass = input ("Enter your password to change: ")
userid = int (input ("Enter your userid: "))
query = ("update userdetails set username = %s ,userpass = %s where userid = %s;")
value = (username,userpass,userid)
cursor.execute(query,value)
conn.commit()
conn.close()
print("okk")

#DELETE
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    database = "userlogin",
    user = "root",
    password = "pass@33")
cursor = conn.cursor()
userid = int(input("Enter a userid to DELETE: "))
query = ("delete  from userdetails where userid = %s;")
value = (userid,)
cursor.execute(query,value)
conn.commit()
conn.close()
print("fine")
'''
