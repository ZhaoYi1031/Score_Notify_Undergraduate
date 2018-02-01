import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

def getScore(username, password):
    #设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cj = http.cookiejar.LWPCookieJar()
    cookie_support = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
    #urllib.request.install_opener(opener)

    #需要POST的数据#
    postdata={
        'username':username,
        'password':password,
        'lt':'LT-460953-QtGskQOlyUIPu2YhP4ib1AL6BquyLD',#需要从页面取
        'execution':'e1s1',
        '_eventId':'submit',
        'submit':'%E7%99%BB%E5%BD%95',
        'code':''
    }

    #header
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        'Referer' : 'https://sso.buaa.edu.cn/login?service=http%3A%2F%2F10.200.21.61%3A7001%2Fieas2.1%2Fwelcome'
    }

    #需要给Post数据编码
    postData = urllib.parse.urlencode(postdata).encode('utf-8')

    #自定义一个请求# 先get下 lt
    req = urllib.request.Request(
                                 'https://sso.buaa.edu.cn/login;jsessionid=A08D2FCD121EE710A23FFC2AF24D02D6?service=http%3A%2F%2F10.200.21.61%3A7001%2Fieas2.1%2Fwelcome'
                                 )

    #访问该链接#
    result = opener.open(req)

    #打印返回的内容#
    result=result.read().decode("utf-8")
    #print (result)
    #找到lt
    ltItem=re.findall('<input.*?name="lt".*?value="(.*?)".*?/>',result,re.S)
    # print (ltItem[0])
    # print (postdata['lt'])
    postdata['lt']=ltItem[0]

    postData = urllib.parse.urlencode(postdata).encode('utf-8')
    req = urllib.request.Request(
                                 'https://sso.buaa.edu.cn/login;jsessionid=A08D2FCD121EE710A23FFC2AF24D02D6?service=http%3A%2F%2F10.200.21.61%3A7001%2Fieas2.1%2Fwelcome',
                                 postData,
                                 headers
                                 )

    #访问该链接#
    result = opener.open(req)

    #打印返回的内容#
    result=result.read().decode("utf-8")

    gradeURL='http://10.200.21.61:7001/ieas2.1/cjcx/queryTyQmcj'
    # get成绩信息
    postdata={'pageXnxq':'2017-20181'}
    postData = urllib.parse.urlencode(postdata).encode('utf-8')

    req = urllib.request.Request(gradeURL,postData)

    #访问该链接#
    result = opener.open(req)

    #打印返回的内容#
    result=result.read().decode("utf-8")
    #print (result)

    soup = BeautifulSoup(result, "lxml")
    #print(soup.find_all(attrs={"class": "list"}))
    listValue = soup.find_all(attrs={"class": "list"})

    ans = {}
    lists = listValue[0].findAll('tr')
    for i in range(1, len(lists)):
        course = lists[i].findAll('td')[4].text#.encode("utf-8")#string
        score = lists[i].findAll('td')[11].text#.encode("utf-8")#string
        #print(course,' ',score)
        ans[course] = score
    return ans




