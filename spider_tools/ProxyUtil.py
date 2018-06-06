# encoding=utf-8
# author: doo

import requests

class ProxyUtil(object):
    #获取代理的接口(代理以IP的形式给出：以大象代理为例(已过期))
    request_url = 'http://vtp.daxiangdaili.com/ip/?tid=557873195286908&protocol=http&category=2&filter=on&num=3'
    ip_list = []

    #遍历代理，判断代理是否可用
    def getProxies(self):
        """
        获取ip代理并存入ip代理池
        :return:
        """
        html = requests.get(self.request_url).content
        for proxy in html.split('\r\n'):
            proxies = {"http": "http://"+proxy}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}  # 构造头部
            try:
                if requests.get(url='http://shop.99114.com', proxies=proxies, headers=headers).status_code == 200:
                    print ('success %s' % proxy)
                    self.ip_list.append(proxy)
                else:
                    print ('fail %s' % proxy)
            except:
                print "Connection failed"
                continue
        return self.ip_list

