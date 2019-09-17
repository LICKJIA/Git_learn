"""
数据库存储文件
数据库存储文件两种策略：
１．存储文件路径（节省数据库空间）
２．存储文件－－　迁移时无需重新指定路径
"""

import pymysql
db = pymysql.connect(host ='localhost',port=3306,user='root',password='123456',database='dict',charset='utf8')
cur = db.cursor()

try:
    # # 存图
    # sql = "insert into image(name,photo,comment) values(%s,%s,%s)"
    # with open('02.jpg','rb') as fd:
    #         data = fd.read()
    #         cur.execute(sql,['02.jpg',data,'no comment'])
    #         db.commit()
    # 取图
    sql = "select * from image"
    cur.execute(sql)
    data =cur.fetchone()
    print(data[1])
    with open(data[1],"wb") as fd:
        fd.write(data[2])
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()
