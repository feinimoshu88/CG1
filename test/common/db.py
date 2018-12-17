import pymysql

class Db:
    connection = pymysql.connect (host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
                                  db='finance_qa',
                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor=connection.cursor()
