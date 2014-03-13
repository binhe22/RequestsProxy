#coding:utf8
import requests
import re
import base64

ips = []
ports = []
http = []
def startRun(num):
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
    print ips, ports, len(ips), len(ports)
    for i in xrange(len(ips)):
        http.append(str(ips[i]+":"+ports[i]))
    return http


if __name__ == "__main__":
    startRun()
