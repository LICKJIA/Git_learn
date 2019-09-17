"""
   编写一个程序,模拟用户注册,登录的数据库行为

   stu->user表

   * 用户名不能重复
   * 要包含用户名和密码字段
"""

import pymysql

class User:
    def __init__(self,database):
        self.db = pymysql.connect(user='root',
                                  passwd='123456',
                                  database=database,
                                  charset='utf8')
        self.cur = self.db.cursor()

    def register(self,name,passwd):
        sql = "select * from login where name=%s"
        self.cur.execute(sql,[name])
        r = self.cur.fetchone()
        # 查找到说明用户存在
        if r:
            return False

        # 插入用户名密码
        sql = "insert into login (name,password) \
        values (%s,%s)"
        try:
            self.cur.execute(sql, [name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()

    def login(self,name,passwd):
        sql = "select * from login \
        where name=%s and password=%s"
        self.cur.execute(sql, [name,passwd])
        r = self.cur.fetchone()
        # 查找到则登录成功
        if r:
            return True



if __name__ == '__main__':
    user = User('dict')

    # if user.register('Abby','123'):
    #     print("注册成功")

    if user.login('Abby','1234'):
        print("登录成功")