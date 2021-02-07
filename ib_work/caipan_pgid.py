##裁判文书网的pageID是一个32次（0-15）数字进行16进制转换后的随机数组合
import random

def uuid():
    uuid = ""
    for i in range(32):

        ten = random.randint(0,15)
        t = hex(ten)
        uuid += t[2]

    return uuid