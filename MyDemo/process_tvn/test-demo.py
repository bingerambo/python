#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import codecs

cwd = os.getcwd()
print(cwd)

# PATH = "C:\\Users\\Binge\\Desktop" + os.path.sep
PATH = cwd + os.path.sep
print(PATH)

# fd = os.open("immoc.txt", os.O_CREAT | os.O_RDWR)

# os.write(fd, b"imooc well")

# str = os.read(fd, 10)

# print(str)

# os.close(fd)
# 
# 
print("================")

f = open("o-dat.txt", 'r', encoding='utf-8', errors='ignore')

content = f.read()
# codecs.encode(content,'utf-8')
print(type(content))
print(content)
f.close()

f2 = open("data-2.txt", "w", encoding="utf-8")
f2.write(content)
f2.close()


# content = content.decode("gbk").encode("utf-8")
# content = content.encode("utf-8")
# codecs.decode(content)
# print(content)

# f3 = codecs.open("data-2.txt", 'r','GBK')
# cont = f3.read()
#
# print(type(cont))
# print(type(codecs.decode(cont)))




# str = "this is string example....wow!!!"
# str = str.encode('base64','strict')

# print ("Encoded String: " + str)
# print ("Decoded String: " + str.decode('base64','strict'))
