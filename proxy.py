#!/usr/bin/env python
#coding:utf8
from gevent import monkey;monkey.patch_socket()
import cnproxy
import coolproxy
import ipcn
from gevent import pool
from gevent.coros import BoundedSemaphore
import requests

cnprxoyGoodUrls = []
coolproxyGoodUrls = []
ipcnproxtGoodUrls = []
p = pool.Pool(100)

cnproxyLock = BoundedSemaphore(1)
coolproxyLock = BoundedSemaphore(1)
ipcnproxyLock = BoundedSemaphore(1)
testUrl = "http://www.baidu.com"

def checkUrls(proxyUrl, testUrl, list, lock):
    try:
        r = requests.get(testUrl, proxies = {"http":proxyUrl}, timeout=3)
        print r.status_code
        if r.status_code == 200:
            lock.acquire()
            list.append(proxyUrl)
            lock.release()
    except Exception, e:
        print "error",e
        try:
            lock.release()
        except:
            print "have releases"
        return

def startCheck(getUrlFunc, goodUrlsList, num, ifnum, lock):
    if ifnum:
        urls = getUrlFunc(num)
    else:
        urls = getUrlFunc()
    print len(urls)
    for i in urls:
        p.spawn(checkUrls, i, testUrl, goodUrlsList, lock)

def startRun():
    p.spawn(startCheck, ipcn.startRun, ipcnproxtGoodUrls, None, 0, ipcnproxyLock)
    #p.spawn(startCheck, cnproxy.startRun, cnprxoyGoodUrls, 5, 1, cnproxyLock)
    p.spawn(startCheck, coolproxy.startRun, coolproxyGoodUrls, 2, 1, coolproxyLock)
    p.join()
    print cnprxoyGoodUrls, coolproxyGoodUrls, ipcnproxtGoodUrls
    returnProxy = cnprxoyGoodUrls + coolproxyGoodUrls + ipcnproxtGoodUrls
    print len(returnProxy)
    return returnProxy
if __name__ == "__main__":
    startRun()



