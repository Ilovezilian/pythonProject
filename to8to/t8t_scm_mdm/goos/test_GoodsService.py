import datetime
import http.client

from my_utils import ListUtils


# @API("goods.queryByIds")
# Map < Integer, Integer > queryByIds( @ NotEmpty @ ArgsName("ids")  List < Integer > ids);
def queryByIds(ids):
    conn = http.client.HTTPConnection("192.168.1.34:40001")

    payloadStr = {"args": {"ids": ids}}
    payload = payloadStr.__str__()

    headers = {
        'content-type': "application/json",
        's': "/biz/t8t-scm-mdm/app",
        'm': "goods.queryByIds",
        'cache-control': "no-cache",
        'postman-token': "94d5b0d6-650d-820f-a980-259f7ee242c5"
    }

    conn.request("POST", "/", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8").__contains__("\"status\":200"))


def test_queryByIds():
    for ids in ListUtils.getNumberLists(1, 1000, 100):
        # print(ids)
        print()
        print("startTime:", datetime.datetime.now().isoformat())
        # time.sleep(1)
        startTime = datetime.datetime.now().timestamp()
        queryByIds(ids)
        endTime = datetime.datetime.now().timestamp()
        print("endTime:", datetime.datetime.now().isoformat())
        print("take time: ", endTime - startTime, "ids.len:", ids.__len__())
        print()


# @API("views.goods.queryAllByFirstGroup2")
#     List<Goods> queryAllByFirstGroup2(@ArgsName("search") Search search);

def queryAllByFirstGroup2():
    import http.client

    conn = http.client.HTTPConnection("192.168.1.34:40001")

    payload = "{\r\n    \"args\":{\r\n       \"search\":{}\r\n    }\r\n}"

    headers = {
        'content-type': "application/json",
        's': "/biz/t8t-scm-mdm/app",
        'm': "views.goods.queryAllByFirstGroup2",
        'cache-control': "no-cache",
        'postman-token': "afddba23-d66d-7958-1ae5-15248b688992"
    }

    conn.request("POST", "/", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8").__contains__("\"status\":200"))


def test_queryAllByFirstGroup2():
    for i in range(4):
        # print(i)
        print()
        print("startTime:", datetime.datetime.now().isoformat())
        # time.sleep(1)
        startTime = datetime.datetime.now().timestamp()
        queryAllByFirstGroup2()
        endTime = datetime.datetime.now().timestamp()
        print("endTime:", datetime.datetime.now().isoformat())
        print("take time: ", endTime - startTime, "i:", i)
        # print("take time: ", endTime - startTime, "ids.len:", ids.__len__())
        print()


if __name__ == '__main__':
    test_queryByIds()
    test_queryAllByFirstGroup2()
