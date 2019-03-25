import http.client
import json
import time


def getFromWeb(page: int):
    conn = http.client.HTTPSConnection("shadmin.to8to.com")

    payload = ""

    headers = {
        # 'host': "shadmin.to8to.com",
        # 'connection': "keep-alive",
        # 'accept': "application/json, text/javascript, */*; q=0.01",
        # 'dnt': "1",
        # 'x-csrf-token': "kXnGwybO9Xy9mPMaNa0bPsVqVV7chykxhuuVL5X3",
        # 'x-requested-with': "XMLHttpRequest",
        # 'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        # 'referer': "https//shadmin.to8to.com/admin/device",
        # 'accept-encoding': "gzip, deflate, br",
        # 'accept-language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        # 'cookie': "uid=wKgBjlt/v1qBu0CMAwksAg==; to8to_cook=OkOcClPzRWV8ZFJlCIF4Ag==; _jzqa=1.3328543590641911300.1536048463.1536048463.1536051159.2; _jzqx=1.1536051159.1536051159.1.jzqsr=to8to%2Ecom|jzqct=/front/index%2Ephp/my/pmatcloseaccount/list.-; to8to_landtime=1543894457; to8tocookieid=85c9b3cdd125d800c2b53287ffd29836264315; to8to_tcode=sz; to8to_tname=%E6%B7%B1%E5%9C%B3; to8to_townid=1130; to8to_fcm_name=shuaishuaipan; to8to_nowpage=http%253A%252F%252Fwww.to8to.com%252Fmy%252Fmall%252Fbatch_list1.php%253FparentName%253D%2525E6%2525B0%2525B4%2526treeName%253DPPR%2525E7%2525AE%2525A1%2526id%253D2078; to8to_sourcepage=http%3A//localhost%3A8070/; to8to_landpage=http%3A//www.to8to.com/com_login.php%3Freferer%3Dhttp%3A//www.to8to.com/my/main_material_order_detail.php%3Fact%3DorderList; sourcepath=b4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Cb4%7Clocalhost%7Cb4%7Cb4%7Clocalhost%7Clocalhost%7Cb4%7Clocalhost%7Clocalhost%7Clocalhost%7Clocalhost%7Clocalhost; Hm_lvt_dbdd94468cf0ef471455c47f380f58d2=1546917131,1546917214,1546917242,1546917249; t8t-it-uid=21216; t8t-it-username=shuai.pan; t8t-it-ticket=p4JSOIelHcgp2ObByN3ZghnNBR1kmva8KiogzPJf9D6gT1Tzr3EVfmph3G9oHiIrLkMcDv_3TfhBNm57CfmFo38XXnO2Fpq01hTjIaHSC9A%2A; t8t-it-certificates=%7B%22operat-tools%22%3A%22b17a49c789cfcb55c7374aa57f610d00%22%2C%22im-pc%22%3A%222011c3646f9f5d2cc13a3cada866fb86%22%2C%22oa-pc%22%3A%2252b9f71997879b8721986673e5b3d78c%22%2C%22dmp%22%3A%22e29765fb6655544be7101e0b14c550d3%22%2C%22shejiben-h5%22%3A%226269d6256e047caa07ab4212d7144e40%22%2C%22to8to-pc%22%3A%22a2cd35868f2d834ed99ac764070fc059%22%2C%22to8to-app%22%3A%229eef49965f75ca66db15176661c50505%22%2C%22qms-h5%22%3A%22055dcd022599fc1f7aeed41a8914f1f6%22%2C%22shejiben-app%22%3A%22bdb84be896f3cb6abf6d5c09b89efa65%22%2C%22oa%22%3A%2223cb404a1737d2ea621da7dadc21a6e8%22%2C%22dsp-pc%22%3A%22bff4eb0705da329d88c517619293cdb7%22%2C%22supplier%22%3A%22ffc7f1af4fee2e3a40ac27a24769c483%22%2C%22h5-app%22%3A%22fdc87198c3130152db24f2279a98fdbc%22%2C%22tumax%22%3A%222121557f23b92c23078f5480329b15b3%22%2C%22tbt-app%22%3A%22461dcd5bf5d97b3d18ec9287ce58e577%22%2C%22shejiben-pc%22%3A%2251c5ac8b971e5f2f667723191c874d2c%22%2C%22tuchat-pc%22%3A%22cb17d9843f8103b2f7f7d40cc4222c18%22%2C%22bhp-pc%22%3A%222bbffc96c2da358917e3d39393688c93%22%2C%22CloudRabbit-app%22%3A%22ea3b1d4d6cdcbce387b62ba61b46c55c%22%2C%22drp-pc%22%3A%22b1938727b0c20ccdcc311649e25da1b6%22%2C%22CloudRabbit-cli%22%3A%22585882c8bb4cf868007e0b3d40fa9d99%22%2C%22im%22%3A%227d3eb9f8fe61f651b4eb89fb5dbd0974%22%2C%22qa-app%22%3A%22a5160a20723ee184f4dcf59cd40b5ed4%22%2C%22pos-app%22%3A%22eb4beb490d8819850f885d63e0b8d5ad%22%2C%22tujingji%22%3A%2202cb1fd43bddad6c514008e0844295cb%22%2C%22supplier-app%22%3A%227dc5c62a4bd65bc2c1037ca190d955f6%22%2C%22ops-console%22%3A%2265655946bde02447f52971ae1883f277%22%2C%22crm-pc%22%3A%22be578dd9f2503e54a32cdc6a643dda17%22%2C%22jietong-pc%22%3A%22eecf083eb147583e947b89f2475a0f52%22%2C%22sinan-pc%22%3A%22e4c56d953a857a3c4c49f51537be4fbb%22%2C%22oa-app%22%3A%22fd5e952eaf5e3202840a7cc5064bd5ed%22%2C%22ads%22%3A%227813e254d54da5ccb94217a96c93013a%22%2C%22web-app%22%3A%226a56b93511ed1c90594b97dd2c801c31%22%2C%22shejiben%22%3A%22cd3b931f127ad86e79086ba94451050b%22%2C%22sso-pc%22%3A%222f86ab132e23bda05365603157528c87%22%2C%22dsp-app%22%3A%2260721dfab919bb11f8cda3f20f4d6164%22%2C%22opgw-pc%22%3A%22dfd641103545e232772ed1f1e7a240be%22%7D; XSRF-TOKEN=eyJpdiI6ImIxcmVYYVhhZHplR2VjRWpxZmVaV1E9PSIsInZhbHVlIjoiYWd3Y2Z6SkdEeVN0dFh2K285WnlIcDNwVUJoK0NscGhYbVBYZlwvY1lFenpydGRGNUNPM3Azdml2Slc3YXoySlwvWGZ4OElySTF2aXFHMlkzdW1IaENmdz09IiwibWFjIjoiOTlhOWQxYzBkYzkzY2UwMTQ1NDkxNzBhYzU0M2U2MTkyZTE2ODRjOTU0NjdlYzg0MzQ4YWYxZmI5Y2Y4NzZmMyJ9; laravel_session=eyJpdiI6IlRmNVh4V3I4bFJ4cGlmdFlhdFptK0E9PSIsInZhbHVlIjoiU1lGVW4rYTJsRlF3THpmN05TellmYTg1alwvUysyalkwY1JiSXJlZ0JlQlU0NG9cL1Q5cVAySk1tdXRuVGxUNXp3MEtzMmZqaXVqTklwdnpIRjBUVGplUT09IiwibWFjIjoiMTcwZWM2Y2I3MzA0YTY3YTQxYjJmZjA5MmU2MzZjMTE4MTBkNjI1OGIyYzFmMDBjYzZkOTQxNjg5ZmEwZjc5YSJ9",
        'cookie': "XSRF-TOKEN=eyJpdiI6ImIxcmVYYVhhZHplR2VjRWpxZmVaV1E9PSIsInZhbHVlIjoiYWd3Y2Z6SkdEeVN0dFh2K285WnlIcDNwVUJoK0NscGhYbVBYZlwvY1lFenpydGRGNUNPM3Azdml2Slc3YXoySlwvWGZ4OElySTF2aXFHMlkzdW1IaENmdz09IiwibWFjIjoiOTlhOWQxYzBkYzkzY2UwMTQ1NDkxNzBhYzU0M2U2MTkyZTE2ODRjOTU0NjdlYzg0MzQ4YWYxZmI5Y2Y4NzZmMyJ9; laravel_session=eyJpdiI6IlRmNVh4V3I4bFJ4cGlmdFlhdFptK0E9PSIsInZhbHVlIjoiU1lGVW4rYTJsRlF3THpmN05TellmYTg1alwvUysyalkwY1JiSXJlZ0JlQlU0NG9cL1Q5cVAySk1tdXRuVGxUNXp3MEtzMmZqaXVqTklwdnpIRjBUVGplUT09IiwibWFjIjoiMTcwZWM2Y2I3MzA0YTY3YTQxYjJmZjA5MmU2MzZjMTE4MTBkNjI1OGIyYzFmMDBjYzZkOTQxNjg5ZmEwZjc5YSJ9",
        # 'cache-control': "no-cache",
    }

    conn.request("GET", "/admin/device/list?page=" + str(page), payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


if __name__ == "__main__":
    total = 145
    # for page in range(total)[1:]:
    #     fileName = "idc_device_" + str(page) + ".json"
    #     f = open(fileName, 'w')
    #     res = getFromWeb(page)
    #     f.write(res)
    #     time.sleep(0.01)

    # sumMap = {}
    # for page in range(total)[1:]:
    #     fileName = "idc_device_" + str(page) + ".json"
    #     f = open(fileName, 'r', encoding='unicode-escape')
    #     strData = f.read()
    #     jsonData = json.loads(strData)
    #     total = jsonData['totalPage']
    #     for device in jsonData['data']:
    #         if sumMap.get(device['sn']) is None:
    #             sumMap[device['sn']] = {'devname': device['devname'], "sum_online": 0, "sum": 0}
    #
    #         tmp = sumMap[device['sn']]
    #         tmp['sum'] += 1
    #         if device['online'] == 1:
    #             tmp['sum_online'] += 1
    #
    #     f.close()
    # f = open("sum_device.json", 'w')
    # f.write(str(sumMap))
    # f.close()
    f = open("sum_device.json", 'r',  encoding='gbk')
    f_read = f.read()
    jsonData = json.loads(f_read)
    f.close()
    import csv

    with open('sum_device.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for key in jsonData.keys():
            # for kkey in jsonData.get(key):
            spamwriter.writerow(jsonData.get(key))


    # f.close()
