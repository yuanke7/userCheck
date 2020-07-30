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
import constant

makeLogFile(__file__)


class UserNameCheck :
    def __init__(self, file_path) :
        '''
        :param file_path: file path
        '''
        with open(file_path, 'r', encoding='utf8') as f :
            data = json.load(f)
        self.fb_lst = data['facebook']
        self.tw_lst = data['twitter']
        self.ins_pub_lst = data['instagram-public']
        self.ins_pri_lst = data['instagram-private']
        self.ytb_lst = data['youtube']

    def fb_check(self, data) :
        '''
        :param data:
        :return:(id, name, status)
        '''
        logger.info("facebook_check")
        fid, f_name = data[0], data[1]
        fb_url = 'https://graph.facebook.com/v4.0/{}?fields=id,fan_count&access_token={}'.format(fid,
                                                                                                 constant.FACEBOOK_AC)
        resp = requests.get(fb_url)
        if 'error' in resp.text :
            logger.error("id:{} name:{} Invaild".format(fid, f_name))
            return (fid, f_name, constant.INVALID)
        else :
            logger.info("id:{} name:{} normal state".format(fid, f_name))
            return (fid, f_name, constant.NORMAL)

    def tw_check(self, data) :
        '''
        :param data:
        :return: (id, name, status)
        '''
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
            logger.error('id:{} name:{} Invaild'.format(tid, t_name))
            # check new name of cur_name
            resp = requests.post('https://tweeterid.com/ajax.php', data={'input' : tid})
            if resp.text != "error" :
                new_name = resp.text.replace('@', '')
                logger.info("id:{} new_name:{}".format(tid, new_name))
                return (tid, new_name, constant.UPDATED)
            else :
                logger.error("id:{} new_name Not Found".format(tid))
                return (tid, t_name, constant.NOTFOUND)
        else :
            logger.info('id:{} name:{} normal state'.format(tid, t_name))
            return (tid, t_name, constant.NORMAL)

    def ins_check(self, data, category) :
        '''
        :param data:
        :param category: private or public
        :return: (id, name, category, status)
        '''
        logger.info("ins_check")
        id, name = data[0], data[1]
        url = "https://graph.facebook.com/v4.0/17841406338772941?fields=business_discovery.username(%s){id,name,username,followers_count,follows_count}&access_token=%s" % (
            name, constant.INSTGRAM_AC)
        headers = {
            'accept - encoding' : 'gzip, deflate, br'
        }
        resp = requests.get(url)
        resp.encoding = resp.apparent_encoding
        # unicode to chinese
        text = resp.text.encode('utf-8').decode("unicode_escape")
        # print(text)
        # print(text.encode('raw_unicode_escape').decode())
        if 'error' in text :
            logger.error('id:{} name:{} Invaild'.format(id, name))
            # Check new name
            headers = {
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                "referer" : "https://commentpicker.com/instagram-username.php"
            }
            params = {
                "userid" : id,
                # "token": 'bca38a84193cf27aa5ba079a8717e73c83087aac10953502f79f7436c963c164'
            }
            url_1 = "https://commentpicker.com/actions/instagram-username-action.php"
            resp = requests.get(url_1, params=params, headers=headers)
            # print(resp.text, type(resp.text))
            new_name = json.loads(resp.text)['username']
            if new_name :
                logger.info("id:{} new_name:{}".format(id, new_name))
                return (id, new_name, category, constant.UPDATED)
            else :
                logger.error("id:{} new_name Not Found".format(id))
                return (id, name, category, constant.NOTFOUND)
        else :
            logger.info('id:{} name:{} normal state'.format(id, name))
            return (id, name, category, constant.NORMAL)

    def ytb_check(self, data) :
        '''
        :param data:
        :return:
        '''
        logger.info("ytb_check")
        id, name = data[0], data[1]
        url = 'https://www.googleapis.com/youtube/v3/channels?part=id&id={}&key={}'.format(id, constant.YOUTUBE_API_KEY)
        # print(url)
        resp = requests.get(url)
        total_results = json.loads(resp.text)['pageInfo']['totalResults']
        if total_results :
            logger.info('id:{} name:{} normal state'.format(id, name))
            return (id, name, constant.NORMAL)
        else :
            logger.error('id:{} name:{} invalid'.format(id, name))
            return (id, name, constant.INVALID)


if __name__ == '__main__' :
    p = UserNameCheck('data.json')
    for data in p.ytb_lst :
        ret_val = p.ytb_check(data)

        # break
