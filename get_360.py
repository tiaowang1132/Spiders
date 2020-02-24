# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import datetime


def sendDingMess(result, time):
    r_msg = result
    if len(r_msg) == 0:
        return
    print "send dingding/n"
    header = {"content-type": "application/json"}
    dingapi = "http://dingding.xxxx"  #this is dingding api for sending message.
    message = {}
    messageBody = str(r_msg) + "\n"
    message['SendWho'] = 'xxx'
    message['Type'] = "ding"
    message['Title'] = "360 %s 安全公告" % (time)
    message['Message'] = messageBody
    message['RemindDesc'] = "GITHUB告警测试"
    JsonMessage = json.dumps(message)
    req = requests.post(dingapi, data=JsonMessage, headers=header, timeout=30)
    print req


def start():
    url = 'https://cert.360.cn/daily'
    headers = {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
               'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    params = {'date': time}
    resp = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    #if there isn't vuln today,just skip
    title= soup.find('div', class_='block-title')
    if 'Vulnerability' in str(title):
        vuls = soup.find('div', class_='block-content').children
        contents = ''
        for child in vuls:
            content = re.sub("<[^>]*>", "", str(child))
            print content
            contents += content
        msg = contents.strip('\n')
        sendDingMess(msg, time)
    else:
        print 'no vuls'


if __name__ == '__main__':
    start()