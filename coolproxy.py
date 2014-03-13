#coding:utf8
import requests
import re
import base64

ips = []
ports = []
http = []
def startRun(num):
    if num>24:
        print "error, num too big"
        return None
    global ips, ports, http
    for i in range(num):
        print i,"pages\n"
        url = 'http://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:%d'
        url = url%i
        r = requests.get(url)
        ip = re.findall('Base64.decode\(\"(.*)\"\)', r.text)
        for i in ip:
            ips.append(base64.decodestring(i))
        ports = ports + re.findall("<td>(\d+)</td>", r.text)
    for i in xrange(len(ips)):
        http.append(str("http://"+ips[i]+":"+ports[i]))
    print http
    return http


if __name__ == "__main__":
    startRun(24)
