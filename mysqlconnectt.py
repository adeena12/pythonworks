"""import pymysql
db=pymysql.connect(host='localhost',user='root',password='adeena2023',database='python')
con=db.cursor()
sql.query="insert into tb1 values(%s,%s,%s)"
val=(14,"meera",21)
con.execute(sqlquery,val)
db.commit()
print("inserted")

import pymysql
id=int(input("enter the id"))
na=int(input("ener the name"))
age=int(input("enter the age"))
db=pymysql.connect(host="localhost",user="root",password="adeena2023",database="python")
mycursor=db.cursor()
sql.query="insert into tb1 values(%s,%s,%s)"
val=(id,na,age)
mycursor.execute(sql,val)
db.commit()
print("inserted completely")


import pymysql
id=int(input("enter the id"))
db=pymysql.connect(host="localhost",user="root",password="adeena2023",database="python")
mycursor=db.cursor()
sql="delete from tb1 wheere id='%id'"%(id)
mycursor.execute(sql)
db.commit()
print("deleted completely")


import pymysql
y=input("do you want to update?")
if y=="yes":
    db = pymysql.connect(host="localhost", user="root", password="adeena2023", database="python")
    id=int(input("enter the id"))
    nm=input("enter the name")
    ag=int(input("enter the age"))
    c=db.cursor()
    sql="update tb1 set name='%s
mycursor.execute(sql)
db.commit()
print("deleted completely")"""


import pymysql
id=int(input("enter the id"))
db=pymysql.connect(host="localhost",user="root",password="adeena2023",database="python")
con=db.cursor()
sql="select *  from tb1 wheere id='%id'"%id
con.execute(sql)
i=con.fetchone()
id =i[0]
name=i[1]
ark=i[2]
print(f"id={i[0]},name={name},age={mark}")
