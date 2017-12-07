# -*- coding: utf-8 -*-
import time

# 标准数据类型

# Number(数字)
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

# String(字符串)
str = '人生苦短,我用python'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

# List(列表)
list = ['人生', 23, 2, 33, '苦短']
tinylist = ['我用', 'python']
print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

# Tuple（元组) 元素不能修改
tuple = ('人生', 73, 22.22, '苦短', 30.9)
tinytuple = ('我用', 'python')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# Dictionary（字典）key唯一
dictionary = {'name': 'zs', 'age': 18, 'sex': '男'}
print(dictionary['name'])  # 获取key对应的value

dictionary['name'] = 'alex'  # 根据key修改value
print(dictionary['name'])

del dictionary['name']  # 删除key
print(dictionary)

dictionary.clear()  # 清空字典
print(dictionary)

del dictionary  # 删除字典
try:
    print(dictionary)
except NameError:
    print('字典不存在')

# 1.cmp(dict1, dict2) 比较两个字典元素。
# 2.len(dict) 计算字典元素个数，即键的总数。
# 3.str(dict) 输出字典可打印的字符串表示。
# 4.type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。

# 1.dict.clear()删除字典内所有元素
# 2.dict.copy()返回一个字典的浅复制
# 3.dict.fromkeys(seq[, val])创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
# 4.dict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值
# 5.dict.has_key(key)如果键在字典dict里返回true，否则返回false
# 6.dict.items()以列表返回可遍历的(键, 值) 元组数组
# 7.dict.keys()以列表返回一个字典所有的键
# 8.dict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# 9.dict.update(dict2)把字典dict2的键/值对更新到dict里
# 10.dict.values()以列表返回字典中的所有值
# 11.pop(key[,default])删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# 12.popitem()随机返回并删除字典中的一对键和值。

# Set（集合）

# 日期和时间

ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 1	time.altzone返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
# 2	time.asctime([tupletime])接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# 3	time.clock( )用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
# 4	time.ctime([secs])作用相当于asctime(localtime(secs))，未给参数相当于asctime()
# 5	time.gmtime([secs])接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
# 6	time.localtime([secs])接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
# 7	time.mktime(tupletime)接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
# 8	time.sleep(secs)推迟调用线程的运行，secs指秒数。
# 9	time.strftime(fmt[,tupletime])接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
# 10 time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')根据fmt的格式把一个时间字符串解析为时间元组。
# 11 time.time( )返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# 12 time.tzset()根据环境变量TZ重新初始化时间相关设置。

# 文件操作
# 标准读取文件版
try:
    f = open('C:\\Users\\zhanxiaolin-n22\\.babel.json', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 精简读取文件版
with open('C:\\Users\\zhanxiaolin-n22\\.babel.json', 'r') as f:
    print(f.read())
    # 逐行读取
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

# 精简版写文件
with open('C:\\Users\\zhanxiaolin-n22\\test.txt', 'w') as f:
    f.write('Hello, world!')

import json

#Json
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json = json.dumps(data)
print(json)


import wx

print(wx.version())

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='world',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # connection.open;
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `city`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        datas = cursor.fetchall()
        for data in datas:
            print(data)
finally:
    connection.close()

time.sleep(5)

from sqlalchemy import create_engine

#创建引擎
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/world", max_overflow=5,encoding='utf-8')
# #执行sql语句
# engine.execute("INSERT INTO user (name) VALUES ('dadadadad')")

result = engine.execute("select * from city")
res = result.fetchall()
print(res)


num = [1,2,3]
a = num.__reversed__()
num.reverse()
print(num)
for b in a :
    print(b)