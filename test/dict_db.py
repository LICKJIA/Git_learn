"""
dict.pyd将字典导入数据库
"""
import pymysql
db = pymysql.connect(host ='localhost',port=3306,user='root',password='123456',database='dict',charset='utf8')
cur = db.cursor()
sql = "insert into words(word,mean) values(%s,%s)"
try:
    with open('dict.txt','r') as fd:
        while True:
            data = fd.readline()
            if not data:
                break
            data_spl=data.split(' ',1)
            for item in data_spl:
                item.strip(" ")
            cur.execute(sql,data_spl)
except Exception as e:
    print(e)
    db.rollback()
db.commit()
cur.close()
db.close()
