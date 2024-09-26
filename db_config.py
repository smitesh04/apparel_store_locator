import pymysql

class DbConfig():
    con = pymysql.Connect(host='localhost', user='root', password='actowiz', database='apparel_store_locator')
    cur = con.cursor(pymysql.cursors.DictCursor)
    data_table = 'data'
    input_table = 'input'
