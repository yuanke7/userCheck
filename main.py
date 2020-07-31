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
import constant
from dbTools import DBTool
from process import UserNameCheck
from MyLibrary.common.mylog import *

makeLogFile(__file__)

if __name__ == '__main__' :
    # read file
    p = UserNameCheck('data.json')
    # open db
    db = DBTool(host='localhost', username='root', password='123456', dbname='usercheck')
    # facebook
    for data in p.fb_lst :
        try :
            ret_val = p.fb_check(data)
            db.updatedb(constant.SQL['fb'] % ret_val)
        except Exception as e :
            logger.error(constant.ERROR_INFO % ('youtube', data))
            logger.error(e)
            continue

    # twitter
    for data in p.tw_lst :
        try :
            ret_val = p.tw_check(data)
            db.updatedb(constant.SQL['tw'] % ret_val)
        except Exception as e :
            logger.error(constant.ERROR_INFO % ('twitter', data))
            logger.error(e)
            continue

    # instgram_pub
    for data in p.ins_pub_lst :
        try :
            ret_val = p.ins_check(data, 'public')
            db.updatedb(constant.SQL['ins'] % ret_val)
        except Exception as e :
            logger.error(constant.ERROR_INFO % ('instgram_pub', data))
            logger.error(e)
            continue

    # instgram_pri
    for data in p.ins_pri_lst :
        try :
            ret_val = p.ins_check(data, 'private')
            db.updatedb(constant.SQL['ins'] % ret_val)
        except Exception as e :
            logger.error(constant.ERROR_INFO % ('instgram_pri', data))
            logger.error(e)
            continue

    # youtube
    for data in p.ytb_lst :
        try :
            ret_val = p.ytb_check(data)
            db.updatedb(constant.SQL['ytb'] % ret_val)
        except Exception as e :
            logger.error(constant.ERROR_INFO % ('youtube', data))
            logger.error(e)
            continue

    db.closedb()
