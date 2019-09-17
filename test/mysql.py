"""
Mysql.py
pymysql示例

链接数据库，获取链接对象db－>　获取游标对象－>执行sql语句－>提交数据库操作——>关闭游标对象－>关闭数据库链接
"""
import pymysql

#　链接数据库

db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='stu',charset='utf8')

# 获取游标（操纵数据库，执行ｓｑｌ语句，返回结果）
cur = db.cursor()

# 执行sql语句

sql = 'insert into class(name,age,gender,score) values("Emmi",17,"w",79)'
# 执行写操作
cur.execute(sql)
# 提交数据库
db.commit()
# 删除
cur.execute("delete from class where name = 'Emmi'")

# 提交数据库
db.commit()




# 获取数据
sql = 'select * from class'
cur.execute(sql)

# 注意游标对象是一个可迭代对象，一次查询类似文件读取操作，游标一条条后移
# # 获取所有查询结果
# all_raw=cur.fetchall()
# print(all_raw)

# 获取多个查询结果

many_raw = cur.fetchmany(2)
print(many_raw)

# 获取一条查询结果
one_raw = cur.fetchone()
print(one_raw)

all_raw=cur.fetchall()
print(all_raw)
cur.close()
db.close()
