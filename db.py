import pymysql
from readConfig import ReadConfig
# from jkutrl.config import Config
from utils.config import Config

host = Config().get ('HOST')
port=Config().get('PORT')
user=Config().get('user')
password=Config().get('password')
db=Config().get('db')
charset=Config().get('charset')

#=====
# host=ReadConfig().get_db("HOST")
# port=int(ReadConfig().get_db("PORT"))
# user=ReadConfig().get_db("user")
# password=ReadConfig().get_db("password")
# db=ReadConfig().get_db("db")
# charset=ReadConfig().get_db("charset")

class Db:
    # connection = pymysql.connect (host='192.168.1.250', port=3306, user='dev_db_user', password='yrSuper001',
    #                               db='finance_hkjf',
    #                               charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    # cursor=connection.cursor()
    connection = pymysql.connect (host=host, port=port, user=user, password=password,db=db,charset=charset, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor ()
