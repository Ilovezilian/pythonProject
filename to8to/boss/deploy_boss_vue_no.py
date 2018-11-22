import datetime
import http.client
import http.client
import time
import zlib

import chardet


# class DeployBossNo():
def deploy_test():
    conn = http.client.HTTPConnection("boss.we.com")

    payload = "{\"ticket_id\":\"35107\"}"

    headers = {
        # 'host': "boss.we.com",
        'connection': "keep-alive",
        # 'content-length': "21",
        # 'accept': "application/json, text/plain, */*",
        # 'origin': "http//boss.we.com",
        # 'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'dnt': "1",
        'content-type': "application/json;charset=UTF-8",
        # 'referer': "http//boss.we.com/index.html",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        'cookie': "_ga=GA1.2.1594600724.1532488623; username=vera.jiang; sessionid=yfevy77jrkduzt9zdza8g3cwt7bu08sw; uid=wKgB3Vv0s5kGXSBzAwUfAg==; env=uat; sessionid_boss=s6puyzxary0vynz2e2qlou4jadj4flbt",
        'cache-control': "no-cache",
    }

    conn.request("POST", "/api/v1/delivery/publish_vue/do_deploy/", payload, headers)

    res = conn.getresponse()
    data = res.read()

    encoding = res.info().get('Content-Encoding')
    html = None
    if encoding is None:
        html = data
    elif encoding == 'gzip':
        html = zlib.decompress(data, 16 + zlib.MAX_WBITS)

    charset = chardet.detect(html)["encoding"]
    ret = html.decode(charset)
    print(ret)
    print(datetime.datetime.now().isoformat())
    return ret


while True:
    res = deploy_test()
    s = "35107"
    if res.__contains__("%s" % s):
        print("潘帅你好！ 工单: %s 正在部署!" % s)
        # break
        time.sleep(1)
    else:
        print("潘帅你好！ 工单: %s 部署完成!" % s)
        break
        time.sleep(1)
