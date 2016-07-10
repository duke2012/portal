import MySQLdb

host='localhost'
user='root'
passwd='123456'
db='flight'

def writeDb(sql):
    """
    连接mysql数据库（写），并进行写的操作，如果连接失败，会把错误写入日志中，并返回false，如果sql执行失败，也会把错误写入日志中，并返回false，如果所有执行正常，则返回true
    """
    try:
        conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="flight",charset="utf8") 
        cursor = conn.cursor()
    except Exception as e:
        print(e)
        return False
    try:
        cursor.execute(sql)
        conn.commit()   #提交事务
    except Exception as e:
        conn.rollback()   #如果出错，则事务回滚
        return False
    finally:
        cursor.close()
        conn.close()
    return True

def readDb(sql):
    """
    连接mysql数据库（从），并进行数据查询，如果连接失败，会把错误写入日志中，并返回false，如果sql执行失败，也会把错误写入日志中，并返回false，如果所有执行正常，则返回查询到
的数据，这个数据是经过转换的，转成字典格式，方便模板调用，其中字典的key是数据表里的字段名
    """
    try:
        conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="flight",charset="utf8") 
        cursor = conn.cursor()
    except Exception as e:
        return False
    try:
        cursor.execute(sql)
        data = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]     #转换数据，字典格式
    except Exception as e:
        return False
    finally:
        cursor.close()
        conn.close()
    return data

