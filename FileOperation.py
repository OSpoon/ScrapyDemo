import os

# 输出文本到文件
import threading
from _thread import start_new_thread
from io import open

a = open('test.txt', 'w')
a.write("""This is 
how you 
create a 
new text 
file""")
a.close()


# 文本追加
def add_some_file(path):
    f = open(path, 'a')
    f.write("\n")
    f.write("This is how you create a new text file")
    f.close()


def make_another_file(path):
    if os.path.isfile(path):
        add_some_file(path)
    else:
        f = open(path, 'w')
        f.write("This is how you create a new text file")
        f.close()


make_another_file('hello.txt')

try:
    f = open('test.txt', "r")
    print(f.read())
except FileNotFoundError:
    print("文件未找到")
finally:
    try:
        f.close()
    except NameError:
        print("文件名称错误")


def print_line_lengths():
    a = open('test.txt', 'r')
    text = a.readlines()
    for line in text:
        print(len(line))
        print(line)


print_line_lengths()


###############################################

# with open('D:\\eclipse-javaee.zip', 'r', encoding='utf8') as f_read,\
#         open('D:\\eclipse-javaee2.zip', 'w', encoding='utf8') as f_write:
#     for line in f_read:
#         f_write.write(line)

def getFileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


def writeFile(args, *kwargs):
    file_read_path = 'D:\\eclipse-javaee.zip'
    file_write_path = 'D:\\eclipse-javaee2.zip'
    ratio_temp = 0
    with open(file_read_path, 'rb') as f_read, \
            open(file_write_path, 'wb') as f_write:
        len_sum = getFileSize(file_read_path)
        for line in f_read:
            f_write.write(line)
            ratio = round(getFileSize(file_write_path) / len_sum * 100, 2)
            if ratio_temp != ratio :
                ratio_temp = ratio
                print(ratio_temp)

# threading.Thread(target=writeFile, args=('Alice',), name='Thread-A').start()
from Crypto.Cipher import AES

with open('key.txt','rb') as f,\
        open('ciphertext.txt','rb') as f2:
    key = f.read()
    obj = AES.new(key, AES.MODE_ECB)
    message = "The answer is no"
    ciphertext = obj.encrypt(key)
    print(ciphertext)
    ciphertext = f2.read()
    obj2 = AES.new(key, AES.MODE_ECB)
    print(obj2.decrypt(ciphertext))