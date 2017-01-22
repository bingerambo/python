#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: html_outputer.py
@time: 2016-11-02 17:24
@description:
"""


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.extend(data)

    def output_html(self, title="Binge-Crawl-Data", name="output.html"):
        with open(name, 'w', encoding='utf-8', errors='ignore') as fout:
            fout.write('<html>')
            fout.write('<head>')
            fout.write("<meta http-equiv='content-type' content='text/html;charset=utf-8'>")
            fout.write('<title>')
            fout.write(title)
            fout.write('</title>')
            fout.write('</head>')
            fout.write('<body>')
            fout.write("<table>")

            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>%s<br><br><br></td>" % data['html_content'])
                fout.write("</tr>")


if __name__ == '__main__':
    pass
