#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 18:51
# @Author  : Jarno_Y
# @Email   : ykq12313@gmail.com
# @File    : main.py
# @Software: PyCharm
'''
Module Introduction
'''
from dbTools import DBTool
from process import UserNameCheck

if __name__ == '__main__':
    p = UserNameCheck('data.json')
    db = DBTool(host='localhost', username='root', password='123456', dbname='usercheck')
    for data in p.fb_lst:
        ret_val = p.fb_check(data)
        db.updatedb("replace into fb(fid, fname, status) values('%s', '%s', '%s')"% ret_val)
        # db = DBTool(host='localhost', username='root', password='123456', dbname='usercheck')
        # db.insertdb("INSERT INTO fb(fid, fname, status)VALUES('%s','%s','%s');" % (arg1, arg2, 3))
    for data in p.tw_lst:
        ret_val = p.tw_check(data)
        db.updatedb("replace into tw(tid, tname, status) values('%s', '%s', '%s')"% ret_val)
    db.closedb()
