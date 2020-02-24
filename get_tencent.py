# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import datetime
import sys
import io

reload(sys)
sys.setdefaultencoding('utf-8')


def sendDingMess(url,content, time):

    print "send dingding/n"
    header = {"content-type": "application/json"}
    dingapi = "http://dingding.xxxx"  # this is dingding api for sending message.
    message = {}
    #change Unicode to str
    content = content.encode('utf-8')
    print type(content)
    messageBody = str(content) + "\n" +  url

    message['SendWho'] = 'xxx'
    message['Type'] = "ding"
    message['Title'] = "腾讯云 %s 安全公告" % (time)
    message['Message'] = messageBody
    message['RemindDesc'] = "GITHUB告警测试"
    JsonMessage = json.dumps(message)
    req = requests.post(dingapi, data=JsonMessage, headers=header, timeout=30)
    print req


def start():
    domain='https://cloud.tencent.com/announce?page=1&categorys=21'
    url = 'https://cloud.tencent.com/announce/ajax'
    headers = {'Connection': 'close', 
               'Content - Type': 'application / json;charset = UTF - 8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    time_bef = (datetime.datetime.now()+datetime.timedelta(hours=-1)).strftime('%Y-%m-%d %H:%M:%S')
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time='2019-04-10 17:11:00'
    data1={"action":"getAnnounceList","data":{"rp":15,"page":"1","categorys":["21"]}}
    resp = requests.post(url,json=data1,headers=headers)
    #print resp.text
    rep= json.loads(resp.text)
    pub_list=rep['data']['rows']
    print pub_list
    for i in range(0,len(pub_list)):
        begintime=pub_list[i]['beginTime']
        if cmp(time,begintime)==-1:
            title= pub_list[i]['title']
            sendDingMess(domain,title, time)



if __name__ == '__main__':
    start()
