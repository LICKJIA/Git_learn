import pymysql

db = pymysql.connect(host='localhost',port=3306,user='root',password ='123456',database ='stu',charset='utf8')

cur = db.cursor()

name = input("Name:")
age = input("Age:")
score = input("Score:")
try:

    # # 必须保证sql语句正确，注意sql语句内的引号
    # sql = "insert into class(name,age,score) value('%s',%s,%s)"%(name,age,score)
    # print(sql)
    # cur.execute(sql)

    # sql 语句可以通过execute传入插入时values值和while　条件，不能用于传递字段　表名等信息

    sql = "insert into class(name,age,score) value(%s,%s,%s)"
    cur.execute(sql,[name,age,score])
    # 修改操作
    sql = "update class set score = 91 where name='Tom'"
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()