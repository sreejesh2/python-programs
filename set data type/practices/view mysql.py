import pymysql
#id = int(input("Enter id"))
#name=input("Enter name :")
#age=int(input("Enter age :"))
# place=input("Enter place :")
db=pymysql.connect(host='localhost',user='root',password='sreejesh',database='sample')
con=db.cursor()
#sqlquery="insert into tab1 values(%s,%s,%s,%s)"
sql="select * from tab1 "
#val=(id,name,age,place)
con.execute(sql)
i=con.fetchall()
for j in i:
    c=list(j)
    print(c[0],c[1],c[2],c[3])
