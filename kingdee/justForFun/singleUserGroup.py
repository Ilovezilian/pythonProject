import http.client
import json


def printJobTitleSet(users):
    jobTitleSet = set()
    for user in users:
        jobTitleSet.add(user["jobTitle"])
    print("jobTitleSet_Count", jobTitleSet.__len__())
    print("jobTitleSet", jobTitleSet)


def printGenderCount(users):
    gender_male_count = 0
    gender_female_count = 0
    for user in users:
        if user["gender"] == 1:
            gender_male_count += 1
        else:
            gender_female_count += 1
    print("male:", gender_male_count)
    print("female:", gender_female_count)


def printGenderInJobCount(users):
    global user
    user_sum = {}
    for user in users:
        jobTitleName = user["jobTitle"]

        if not user_sum.keys().__contains__(jobTitleName):
            user_sum[jobTitleName] = {"total": 0, "male": 0, "female": 0}

        user_sum[jobTitleName]["total"] += 1
        if user["gender"] == 1:
            user_sum[jobTitleName]["male"] += 1
        else:
            user_sum[jobTitleName]["female"] += 1
    print()
    for sum_key in user_sum.keys():
        print(user_sum[sum_key], '\t', sum_key)


def fetchFromJsonFile():
    with open("singleUserGoupUsers.json", "rb") as f:
        object = f.read()
        loads = json.loads(object)
        return loads["data"]["users"]


def fetchFromWebRequest(page=0, size=200):
    conn = http.client.HTTPConnection("103.41.165.62:443")

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "cookie": "JSESSIONID=1f4hrrsgjniogygkvnxbrrr4l; logintype5dba5d68e4b00ea1ac7cc11b=0; cd=yunzhijia.com; cn=383cee68-cea3-4818-87ae-24fb46e081b1; cu=5dba5d68e4b00ea1ac7cc11b; webLappToken=\"RTXcirUwxXcc3b3S8%2Fdq1TdxXv%2FGyMJVdyX1gIu9mdPOBs40EKs16TD4VxMWJLmsBBKXwwCLQqlxVKkyF7l1cEpNEJ58hMH6B2r6besa8GKO4p43ct6oH%2Fnu6tB9gaQY\"; __att_token=Ez3cJ9kDY095kuYiAjt8hk8KX1SBaIGo; href=https%3A%2F%2Fwww.yunzhijia.com%2Fhome%2F%3Fm%3Dopen%26a%3Dlogin%26redirectUrl%3D%252Fcloud-office%252Fpc%252F%253Fsync_networkid%253D383cee68-cea3-4818-87ae-24fb46e081b1; bad_idce3d5ef0-6836-11e6-85a2-2d5b0666fd02=e1cd24f1-27a0-11ea-92aa-19237b49375f; nice_idce3d5ef0-6836-11e6-85a2-2d5b0666fd02=e1cd24f2-27a0-11ea-92aa-19237b49375f; last_page=/microblog; _jzqc=1; _qzjc=1; __loginType=; redirectUrl=; toweibologin=login; Hm_lvt_45f5f201f5af9cfeffd1f82177d2cceb=1588315739; Hm_lpvt_45f5f201f5af9cfeffd1f82177d2cceb=1590647460; _jzqx=1.1589878500.1593416528.2.jzqsr=login%2Emykingdee%2Ecom|jzqct=/login.jzqsr=yunzhijia%2Ecom|jzqct=/home/; redirectIndexUrl=/cloud-office/pc/index.html; _47d8a=http://10.86.74.161:12088; _ebcef=http://10.86.54.136:3011; sync_networkid=383cee68-cea3-4818-87ae-24fb46e081b1; sync_userid=5dba5d68e4b00ea1ac7cc11b; _936c5=http://10.86.46.203:10092; Hm_lvt_a96914087b350d1aa86c96cdbf56d5e5=1604373676; _jzqa=1.4599815190535756000.1579512272.1602324047.1604373676.16; _qzja=1.536505478.1579512272115.1602324046631.1604373676401.1602324046631.1604373676401..0.0.41.15; Hm_lpvt_a96914087b350d1aa86c96cdbf56d5e5=1605160935; uuid=a13e3e7c-85a4-4d12-a9e7-791cb0dcaefa; gl=a94d30b4-27d0-476a-9516-ccac9f6514b1; at=7f0ab1ca-9eae-4a06-b0ba-2e0adfdb727d; tribenews-sid=s%3AeNOoTjmf_VXlfYtqxbw-98szA-ZG9qFK.1X6D1DslcAXulZrcxlsBQPv9Q7t%2FhDNlvlMCwtxQmKU; _5ed68=http://10.86.45.54:13134"
    }
    payload = {
        "groupId": "5fa240f7e4b0c99e26e72712",
        "offset": page,
        "count": size
    }

    conn.request("POST", "/", payload, headers)

    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))

    return data.decode("utf-8")


def printNameAndFirstNameCount(users):
    nameSet = []
    for user in users:
        if user["gender"] == 2:
            nameSet.append(user["name"])
    nameSet.sort()
    print(nameSet)
    nameSum = {}
    for name in nameSet:
        firstName = name[0]
        if not nameSum.keys().__contains__(firstName):
            nameSum[firstName] = 0
        nameSum[firstName] += 1

    # for nameSumKey in nameSum.keys():
    #     print(nameSumKey, nameSum[nameSumKey])

    names = []
    for nameSumKey in nameSum.keys():
        names.append({"firstName": nameSumKey, "count": nameSum[nameSumKey]})

    names.sort(key=lambda x: x["count"], reverse=True)
    print(names)

    names = []
    for nameSumKey in nameSum.keys():
        names.append((nameSumKey, nameSum[nameSumKey]))

    names.sort(key=lambda x: x[1], reverse=True)
    for name in names:
        print(name)


if __name__ == "__main__":
    users = fetchFromJsonFile()
    # users = fetchFromWebRequest(0, 200)

    print("users_count", len(users))
    printJobTitleSet(users)
    printGenderCount(users)
    printGenderInJobCount(users)
    printNameAndFirstNameCount(users)
