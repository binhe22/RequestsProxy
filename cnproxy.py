#coding:utf8
import requests
import re
import base64

ips = []
ports = []
http = []

atonDic = {"v":"3", "c":"1", "a":"2", "r":"8", "q":"0", "m":"4", "l":"9", "w":"6", "b":"5", "i":"7"}

def toPort(p):
    print p
    port=""
    try:
        for i in p:
            if i != "+":
                port = port + atonDic[i]
        return port
    except Exception:
        return "80"

def startRun(num):
    global ips, ports, http
    if(num > 10):
        return 0
    for i in range(num):
        print i,"pages\n"
        url = 'http://www.cnproxy.com/proxy%d.html'
        url = url%i
        r = requests.get(url)
        ip = re.findall('\d+\.\d+\.\d+\.\d', r.text)
        for i in ip:
            ips.append(str(i))
        port =  re.findall('document.write\(":"(.*)\)',r.text)
        for i in port:
            ports.append(toPort(i))
    for i in xrange(len(ips)):
        http.append(str(ips[i]+":"+ports[i]))
    print http
    return http

if __name__ == "__main__":
    startRun(2)
