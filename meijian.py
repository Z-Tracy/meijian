import requests
import urllib.parse
import json
import time
import random
from urllib.request import urlretrieve
import re
import urllib.request
import http.cookiejar
import urllib


def getjson(url,name):
    headers = {
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.8,zh-HK;q=0.6",
        'AlexaToolbar-ALX_NS_PH': "AlexaToolbar/alx-4.0.1",
        'Connection': "keep-alive",
        'Content-Length': "60",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': "app.meijian.io",
        'Origin': "http://app.meijian.io",
        'Referer': "http://app.meijian.io/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest"
    }
    # time.sleep(int(random.uniform(15, 30)))
    # while res:
    p = 1
    querystring = {"key": urllib.parse.quote(name), "p": "1", "l": "40", "sortType": "0"}
    # s = requests.Session()
    # try:
    #
    # except Exception:
    #     print(Exception)
    res = requests.request("POST", url,data=json.dumps(payload), headers=headers, params=querystring,cookies=cookies)
    print(res.json())
    # print(res)

    #  进入itemSearchNavigation
def itemSearchNavigation():
    url = r'http://app.meijian.io/api/0.2/search/itemSearchNavigation'
    headers ={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-HK;q=0.6',
        'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0.1',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'app.meijian.io',
        'Origin': 'http://app.meijian.io',
        'Referer': 'http://app.meijian.io/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    res = requests.post(url,headers,cookies=cookies)
    print(res.text,res.cookies)
def Paser(imgs):
    n = 1
    for img in imgs:
        url = 'http://m1.cdn.imeijian.cn/{0}@!800wh2'.format(img)
        urlretrieve(url,'{0}.png'.format(n))
        n +=1
        time.sleep(.5)

def login(username,pwd):

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-HK;q=0.6',
        'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0.1',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'app.meijian.io',
        'Origin': 'http://app.meijian.io',
        'Referer': 'http://app.meijian.io/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    cj = http.cookiejar.MozillaCookieJar('cookie.txt')

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    namepwd = {'username': username, 'pwd': pwd}
    data = urllib.parse.urlencode(namepwd).encode('ascii')
    print(data)
    url = 'http://app.meijian.io/api/0.2/account/signin/pwd'
    req = urllib.request.Request(url, data=data, headers=headers)
    # res = urllib.request.urlopen(req).read().decode('utf-8')
    # print(res)
    r = opener.open(req)
    cj.save()
    url2 = 'http://app.meijian.io/api/0.2/search/items'
    # url2 = 'http://app.meijian.io/api/0.2/search/items'
    page = 21
    while True:
        data2 = {
            'key': '配饰',
            'p': page,
            'l': '40',
            'sortType': '0'
        }
        data2 = urllib.parse.urlencode(data2).encode('ascii')
        print(data2)
        req2 = urllib.request.Request(url2, data=data2, headers=headers)
        # req2 = urllib.request.Request(url2)
        # print(req2)
        res2 = opener.open(req2).read().decode('utf-8')
        getimg(res2,page)
        page += 1
        time.sleep(10)
def getimg(res2,page):
    # with open('d:\meijian2.txt', 'r') as f:
    #     t = f.read()
    pattern = re.compile('img":"(.*?)","boardId')
    res = re.findall(pattern,res2)
    print(res)
    n = 0

    for i in res:
        num = (page-1)*40 + n
        hou = i.split('.')[-1]
        url =  'http://m1.cdn.imeijian.cn/{0}@!800wh2'.format(i)
        print((url,'{0}.{1}'.format(num,hou)))
        urlretrieve(url,'{0}.{1}'.format(num,hou))
        n += 1
        time.sleep(1)


if __name__ =='__main__':

    username= yourusn
    pwd = yourpwd
    login(username,pwd)
    # getimg(js)