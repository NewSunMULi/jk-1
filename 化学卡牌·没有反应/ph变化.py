import matplotlib.pyplot as plt
import math
import pymysql


# 定义一个函数
# 这个函数用来创建连接(连接数据库用）
def mysql_db():
    # 连接数据库肯定需要一些参数
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="z555r5555"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userinfo")
    print(cursor.fetchall())


if __name__ == '__main__':
    mysql_db()