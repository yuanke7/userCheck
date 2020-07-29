#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 10:12
# @Author  : Jarno_Y
# @Email   : ykq12313@gmail.com
# @File    : process.py
# @Software: PyCharm
'''
Module Introduction
'''
from MyLibrary.common.mylog import *
import requests, json

makeLogFile(__file__)


class UserNameCheck :
    def __init__(self, file_path) :
        with open(file_path, 'r', encoding='utf8') as f :
            data = json.load(f)
        self.fb_lst = data['facebook']
        self.tw_lst = data['twitter']

    def fb_check(self, data) :
        logger.info("facebook_check")
        AC = "EAAZAlx26seVwBAHZBYx5gpOY06GHZBor7Dix5ebLsjtKg8CMvlz90vhTt7ZCXI5XtdnQ6iUcuA9znJ15zAhLjQcP3oipSy9s4W0nnJCBmBlvLxZB9vi27cSnBQY7uVAAzF3ab9kjAk1tnNGsxT6jBF7xBjJNp3zghzHhKPvAWoQZDZD"
        fid, f_name = data[0], data[1]
        fb_url = 'https://graph.facebook.com/v4.0/{}?fields=id,fan_count&access_token={}'.format(fid, AC)
        resp = requests.get(fb_url)
        if 'error' in resp.text :
            logger.error("id:{} name:{} expired".format(fid, f_name))
            return (fid, f_name, 'Expired')
        else :
            logger.info("id:{} name:{} normal".format(fid, f_name))
            return (fid, f_name, 'No change detected')

    def tw_check(self,data) :
        logger.info("twitter_check")
        headers = {
            'authorization' : 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        }
        tid, t_name = data[0], data[1]
        t_url = 'https://api.twitter.com/graphql/-xfUfZsnR_zqjFd-IfrN5A/UserByScreenName?variables=%7B%22screen_name%22%3A%22{}%22%2C%22withHighlightedLabel%22%3Atrue%7D'.format(
            t_name)
        resp = requests.get(t_url, headers=headers)
        # print(resp.text)
        if 'errors' in resp.text :
            logger.error('id:{} name:{} expired'.format(tid, t_name))
            # check new name of cur_name
            resp = requests.post('https://tweeterid.com/ajax.php', data={'input' : tid})
            if resp.text != "error" :
                new_name = resp.text.replace('@', '')
                logger.info("id:{} new_name:{}".format(tid, new_name))
                return (tid, new_name, 'Updated')
            else :
                logger.error("id:{} new_name Not Found".format(tid))
                return (tid, t_name, 'New name not found')
        else :
            logger.info('id:{} name:{} normal'.format(tid, t_name))
            return (tid, t_name, 'No change detected')

if __name__ == '__main__' :
    p = UserNameCheck('data.json')
    for data in p.fb_lst:
        ret_val = p.fb_check(data)
    for data in p.tw_lst:
        ret_val = p.tw_check(data)