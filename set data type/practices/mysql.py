import pymysql
id = int(input("Enter id"))
# name=input("Enter name :")
# age=int(input("Enter age :"))
# place=input("Enter place :")
db=pymysql.connect(host='localhost',user='root',password='sreejesh',database='sample')
con=db.cursor()
#sqlquery="insert into tab1 values(%s,%s,%s,%s)"
sql="delete from tab1 where id='%d'"%id
#val=(id,name,age,place)
con.execute(sql)
db.commit()
print("deleted successfully")
