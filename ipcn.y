#coding:utf8
import requests
import re
import base64


def startRun():
    httpTmp = []
    http = []
    url = 'http://proxy.ipcn.org/proxylist.html'
    r = requests.get(url)
    httpTmp = re.findall('\d+\.\d+\.\d+\.\d:\d+', r.text)
    for i in httpTmp:
        http.append(str(i))
    print http
    return http


if __name__ == "__main__":
    startRun()
