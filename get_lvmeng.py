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
    dingapi = "http://dingding.xxxx"  #this is dingding api for sending message.
    message = {}
    #change Unicode to str
    content = content.encode('utf-8')
    print type(content)
    messageBody = str(content) + "\n" +  url

    message['SendWho'] = 'xxx'
    message['Type'] = "ding"
    message['Title'] = "绿盟 %s 安全公告" % (time)
    message['Message'] = messageBody
    message['RemindDesc'] = "GITHUB告警测试"
    JsonMessage = json.dumps(message)
    req = requests.post(dingapi, data=JsonMessage, headers=header, timeout=30)
    print req


def start():
    domain='https://www.nsfocus.com.cn/'
    url = 'http://www.nsfocus.com.cn/research/threatintelligence.html'
    headers = {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
               'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

    resp = requests.get(url,headers=headers)
    res=resp.text.encode("ISO-8859-1").decode("utf-8")
    soup = BeautifulSoup(res, 'lxml')
    #get current time
    #time = datetime.datetime.now().strftime('%Y-%m-%d')

    #judging whether new vulns appears.
    print soup.find('ul',class_='vul_list')
    times = soup.select('.vul_list li span')
    a_list = soup.select('.vul_list li a')
    #print a_list
    #print time
    #list=[u'/content/details_141_2939.html\n', u'/content/details_141_2944.html\n', u'/content/details_141_2942.html\n', u'/content/details_141_2941.html\n', u'/content/details_141_2940.html\n', u'/content/details_141_2944.html\n', u'/content/details_141_2942.html\n', u'/content/details_141_2941.html\n', u'/content/details_141_2940.html\n', u'/content/details_141_2939.html\n', u'/content/details_141_2944.html\n', u'/content/details_141_2942.html\n', u'/content/details_141_2941.html\n', u'/content/details_141_2940.html\n', u'/content/details_141_2939.html\n']
    with io.open('lvmeng.txt','r+') as f:
        lines = f.readlines()
        print lines
        for i in range(0,len(times)):
            content=a_list[i]['title']
            time=times[i].text
            url1=a_list[i]['href']
            url1=url1+'\n'
            full_url = domain + url1
            if url1 in lines:
                print url1+'youle\n'
            else:
                print url1 + 'meiyou\n'
                f.write(url1.decode('utf-8'))
                sendDingMess(full_url, content, time)
            print content



if __name__ == '__main__':
    start()