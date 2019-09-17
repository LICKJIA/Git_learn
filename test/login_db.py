import pymysql

class User:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", port=3306, user='root', password='123456',database='dict',
        charset='utf8')
        self.cur = self.db.cursor()

    def login(self,tel,pwd):

        try:
            sql = "select * from login where tel = %s and password = %s"
            self.cur.execute(sql,[tel,pwd])
            data = self.cur.fetchone()
            if not data:
                print("用户不存在！")
            else:
                print("%s,欢迎回来"%data[1])
        except Exception as e:
          print(e)

    def register(self, name,tel, passwd):
        try:
            sql = "select * from login where tel = %s"
            self.cur.execute(sql, [tel])
            data = self.cur.fetchone()
            if  data:
                print("用户已存在！")
            else:
                sql = "insert into login(name,tel,password) values(%s,%s,%s)"
                self.cur.execute(sql,[name,tel,passwd])
                self.db.commit()
                print("注册成功")
        except Exception as e:
            print(e)
    def __del__(self):
        self.cur.close()
        self.db.close()


if __name__=='__main__':
    user = User()
    user.register('Emmi','13529872237','123456')
    user.login("13529872237",'123456')