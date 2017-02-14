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
    # -F 打包成一个exe文件
    # -w 使用窗口，无控制台
    # -c 使用控制台，无窗口
    # --icon = 图标路径
    # --upx-dir 使用upx压缩
    # upx391w ups程序目录文件路径


    # opts = ['tvn_process.py', '-F']
    opts = ['tvn_process.py', '-F', '-w']
    # opts = ['tvn_process.py', '-F', '-c']
    # opts = ['tvn_process.py', '-F', '-w', '--upx-dir', 'upx391w']
    # opts = ['tvn_process.py', '-F', '-w','--icon=tvn_process.ico','--upx-dir','upx391w']

    run(opts)
