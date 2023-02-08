import pymysql
id = int(input("Enter id"))
name=input("Enter name :")
age=int(input("Enter age :"))
# place=input("Enter place :")
db=pymysql.connect(host='localhost',user='root',password='sreejesh',database='sample')
con=db.cursor()
#sqlquery="insert into tab1 values(%s,%s,%s,%s)"
sql="update tab1 set Name='%s' ,Age='%d' where id='%d'"%(name,age,id)
#val=(id,name,age,place)
con.execute(sql)
db.commit()
print("Updated successfully")