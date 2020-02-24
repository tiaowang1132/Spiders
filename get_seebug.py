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
    dingapi = "http://dingding.xxxx"  # this is dingding api for sending message.
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
    domian='https://www.seebug.org/'
    url = 'https://www.seebug.org/vuldb/vulnerabilities'
    headers = {
               'Accept-Encoding': 'gzip, deflate',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
             'Cookie' : '__jsluid=240f35448a7af0276aey30bee2f467y6;__jsl_clearance=1565947863.546|0|ppg%2BEsiJtVU42KRQpafdQut6o%2BY%3D'}

    time = datetime.datetime.now().strftime('%Y-%m-%d')
    #requests.set()
    resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, 'html.parser')
    #print soup.text
    # if there isn't vuln today,just skip
    len1=len(soup.select('tbody tr td'))
    len2 = len(soup.select('tbody tr td a'))
    i=0
    with open('seebug.txt', 'r+') as f:
        lines = f.readlines()
        print lines
        while i < len1:
            time= soup.select('tbody tr td')[i+1].text
            print time
            content = soup.select('tbody tr td ')[i+3]
            url1=content.find('a')['href']
            print url1
            url1 = url1 + '\n'
            full_url1=domian+url1
            title = content.text
            print title
            if url1 in lines:
                print url1+'youle\n'
            else:
                print url1 + 'meiyou\n'
                f.write(url1.decode('utf-8'))
                full_url1 = domian + url1
                #sendDingMess(url1, content, time)
            print content
            i+=6


if __name__ == '__main__':
    start()