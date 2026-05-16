#Install mysql-connector
#Install mysql-connector-pyton packages 
#Implement the conenctivity code

import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    database="userlogin",
    user="root",
    password="pass@33",
    )

cursor = conn.cursor()
query = "select * from userdetails"
cursor.execute(query)

result = cursor.fetchall()
for r in result:
    print(r)
    
print("CONNECTION SUCCESSFUL!!!")
