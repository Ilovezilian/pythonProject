import datetime
import http.client

from my_utils import ListUtils


#    @API("views.purchase.price.detail.query")
#     JSONObject goodsPricePurchaseDetailQuery(@ArgsName("args") JSONObject args);
def goodsPricePurchaseDetailQuery(ids):

    conn = http.client.HTTPConnection("192.168.1.34:40001")

    payload = {
        "args": {
            "args": {
                "ids": ids
            }
        }
    }

    headers = {
        'content-type': "application/json",
        's': "/biz/t8t-scm-mdm/app",
        'm': "views.purchase.price.detail.query",
        'cache-control': "no-cache",
        'postman-token': "9bbc3e9f-8613-864a-8e9c-1a3b44b7fdd9"
    }

    conn.request("POST", "/", payload.__str__(), headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))

    print(data.decode("utf-8").__contains__("\"status\":200"))


def test_goodsPricePurchaseDetailQuery():
    for ids in ListUtils.getNumberLists(1, 1000, 100):
        # print(ids)
        print()
        print("startTime:", datetime.datetime.now().isoformat())
        # time.sleep(1)
        startTime = datetime.datetime.now().timestamp()
        goodsPricePurchaseDetailQuery(ids)
        endTime = datetime.datetime.now().timestamp()
        print("endTime:", datetime.datetime.now().isoformat())
        print("take time: ", endTime - startTime, "ids.len:", ids.__len__())
        print()


if __name__ == '__main__':
    test_goodsPricePurchaseDetailQuery()
