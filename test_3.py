'''
@author：KongWeiKun
@file: test_3.py
@time: 17-6-16 上午4:18
@contact: 836242657@qq.com
'''
'''
将激活码存入到MySQL数据中
'''
import uuid
import pymysql
def ActivationCode(num):
    codeList=[]
    for i in range(num):
        code=str(uuid.uuid4()).replace('-','').upper()
        while code in codeList:
            code=str(uuid.uuid4()).replace('-','').upper()
        codeList.append(code)
    return codeList
def StoreInMysql(codelist):
    try:
        con=pymysql.connect("localhost","root","******","*****")
        cursor=con.cursor()

    except BaseException as e:
        print(e)
    else:
        try:
           for code in codelist:
               cursor.execute('insert into code(code) VALUES(%s)',(code))
               cursor.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cursor.close()
        con.close()
if __name__ == '__main__':
    StoreInMysql(ActivationCode(200))
    print("ok!")