#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: rambo.py
@time: 2016-09-23 9:21
"""
__author__ = "binge"


def _private_1(name):
    print("private func1:", name)


def func(name):
    print("this is rambo module->func call")
    _private_1(name)


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

f = open("immoc.txt", "r+")
print(f)
# out = f.read()
# out = True
# while (out):
#     out = f.readline()
#     print(out.strip())

# out = f.readlines()
# for item in out:
#     print(item)
# print(out)


for item in iter(f):
    print(item.strip())
f.close()
