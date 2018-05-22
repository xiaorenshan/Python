import pymysql.cursors
import string
from random import sample

element = string.digits+string.ascii_uppercase
Coupon_list = []
i = 1
while i <= 50:
    Coupon_list.append( ''.join(sample(element,10)))
    i += 1

connect = pymysql.connect(host='47.94.85.128',port=3306,user='test',password='P@ssw0rd',db='test',use_unicode=True)
cursor = connect.cursor()
sql = ("insert into Coupon (id,Number) values ('%d', '%s')")
i = 0
while i < 50:
    date = (i,Coupon_list[i])
    cursor.execute(sql % date)
    connect.commit()
    i += 1
cursor.close()
connect.close()