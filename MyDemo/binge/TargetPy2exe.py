#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: TargetPy2exe.py.py
@time: 2017-02-07 11:21
@description: convert py to exe by pyinstaller
"""

from PyInstaller.__main__ import run

if __name__ == '__main__':
    # 设置打包exe参数：目标py、打包参数
    # opts = ['squre-turtle.py', '-F']
    # opts = ['squre-turtle.py', '-F','-w']
    opts = ['squre-turtle.py', '-F', '-w','--upx-dir','upx391w']
    # opts = ['squre-turtle.py', '-F', '-w','--icon=squre-turtle.ico','--upx-dir','upx391w']

    run(opts)
