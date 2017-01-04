#coding:utf-8

import lxml.html
import requests
import json

def data_getter():
    search_key = range(1,48)
    pageurl = "http://www.hospital.or.jp/shibu_kaiin/"
    for key in search_key:
        pagesource = requests.get(pageurl + "?sw=%d&sk=1"%key).text
        root = lxml.html.fromstring(pagesource)
        f = open("./data/test%d.txt"%key,"w")
        f.write(pagesource)
        f.close()

if __name__=="__main__":
    data_getter()
