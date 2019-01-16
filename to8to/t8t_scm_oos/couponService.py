import http.client
import json

from to8to.t8t_scm_oos.oos_mysql import OOSMySql

conn = http.client.HTTPConnection("192.168.3.58:40001")


def getCoupons(shopId: int):
    json = {
        "args": {
            "searchCondition": {
            },
            "shopId": shopId,
            "page": 1,
            "size": 10
        }
    }

    payload = json.__str__()

    headers = {
        'content-type': "application/json",
        's': "/biz/t8t-scm-oos/app",
        'm': "views.business.marketingServiceForUI.getCoupons",
        'rpc-uid': "11",
        'cache-control': "no-cache",
        'postman-token': "157f575f-86b1-ba07-c433-d7180be824db"
    }

    conn.request("POST", "/", payload, headers)

    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))

    return data.decode("utf-8")



if __name__ == '__main__':
    test = OOSMySql()
    test.connect()
    for shopId in test.get_shop_ids():
        coupons = getCoupons(shopId)
        heihei = json.loads(coupons)
        if heihei['error'] != '供应商信息不存在':
            print("shopId = ", shopId, " coupons = ", coupons)
