#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 16:49
# @Author  : Jarno_Y
# @Email   : ykq12313@gmail.com
# @File    : constant.py
# @Software: PyCharm
'''
constant
'''
#
FACEBOOK_AC = "EAAZAlx26seVwBAHZBYx5gpOY06GHZBor7Dix5ebLsjtKg8CMvlz90vhTt7ZCXI5XtdnQ6iUcuA9znJ15zAhLjQcP3oipSy9s4W0nnJCBmBlvLxZB9vi27cSnBQY7uVAAzF3ab9kjAk1tnNGsxT6jBF7xBjJNp3zghzHhKPvAWoQZDZD"

INSTGRAM_AC = "EAAZAlx26seVwBAHZBYx5gpOY06GHZBor7Dix5ebLsjtKg8CMvlz90vhTt7ZCXI5XtdnQ6iUcuA9znJ15zAhLjQcP3oipSy9s4W0nnJCBmBlvLxZB9vi27cSnBQY7uVAAzF3ab9kjAk1tnNGsxT6jBF7xBjJNp3zghzHhKPvAWoQZDZD"

YOUTUBE_API_KEY = "AIzaSyD76JCSGXmMO-_rlAL_yGJuW_ZqsJX33Og"

# sql
SQL = {
    'fb' : "replace into fb(fid, fname, status) values('%s', '%s', '%s')",
    'tw' : "replace into tw(tid, tname, status) values('%s', '%s', '%s')",
    'ins' : "replace into ins(insid, insname, category, status) values('%s', '%s', '%s' , '%s')",
    'ytb' : "replace into ytb(yid, yname, status) values('%s', '%s', '%s')",
}

# status
INVALID = 'Invaild'
NORMAL = 'Normal state'
UPDATED = 'Updated'
NOTFOUND = 'New name not found'

# info
ERROR_INFO = "%s check: An error occurred while operating %s"
