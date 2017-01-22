#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: html_outputer.py
@time: 2016-10-27 9:43
"""


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html', 'w', encoding='utf-8', errors='ignore') as fout:
            fout.write('<html>')
            fout.write('<head>')
            fout.write("<meta http-equiv='content-type' content='text/html;charset=utf-8'>")
            fout.write('<title>')
            fout.write('百科数据采集')
            fout.write('</title>')
            fout.write('</head>')
            fout.write('<body>')
            fout.write("<table>")

            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td>%s</td>" % data['title'])
                fout.write("<td>%s</td>" % data['summary'])
                fout.write("</tr>")

            fout.write("</table>")
            fout.write('</body>')
            fout.write('</html>')
