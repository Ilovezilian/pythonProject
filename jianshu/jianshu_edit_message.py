import http.client
import zlib

import chardet

conn = http.client.HTTPSConnection("www.jianshu.com")

payload = ""

headers = {
    'connection': "keep-alive",
    'accept': "application/json",
    'dnt': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    'referer': "https//www.jianshu.com/writer",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    'cookie': "__yadk_uid=lsVy75eBHyVU7MmSONSw5wF3gkeLLRQM; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1541126190,1541467034,1542680843,1542681047; locale=zh-CN; default_font=font2; remember_user_token=W1sxMjE1MjMyXSwiJDJhJDEwJEhEaWxaMlBYNGUxTkVsVmloNGMxYnUiLCIxNTQyNjgxMTYwLjI1OTY4OTgiXQ%3D%3D--785c671d4d0a703d6e383649e329babc963fd3ee; _m7e_session=b91514d6b4eb92b2d3c1e9539dde4306; read_mode=night; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22164b2ef4477815-0d3851d5afae38-6114147a-2073600-164b2ef44782be%22%2C%22%24device_id%22%3A%22164b2ef4477815-0d3851d5afae38-6114147a-2073600-164b2ef44782be%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1542682768",
    'cache-control': "no-cache",
    'postman-token': "6c124182-18cd-db48-6a6e-0a708632d307"
    }

conn.request("GET", "/author/notes/13945219/content", payload, headers)

res = conn.getresponse()
data = res.read()

encoding = res.info().get('Content-Encoding')
if encoding == 'gzip':
    html = zlib.decompress(data, 16 + zlib.MAX_WBITS)

charset = chardet.detect(html)["encoding"]
print(charset)
print(html.decode(charset,'ignore'))
# print(data.decode("utf-8"))




