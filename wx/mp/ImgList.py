import json


def readJsonFile():
    with open('img/img_origin.json', 'rb') as f:
        data = f.read()
        return json.loads(data)


def getItems(datas):
    result = []
    for data in datas:
        for item in data['page_info']['file_item']:
            result.append(item)

    return result


def sortItems(fileItems):
    fileItems.sort(key=lambda dictionary: dictionary['file_id'], reverse=False)


def writeFile(fileItems):
    start = False
    with open('img/img_item.json', 'w') as f:
        f.write("[\r")
        for item in fileItems:
            aRow = json.dumps(item, ensure_ascii=False)
            if not start:
                start = True
            else:
                aRow = ',' +aRow
            f.write(aRow + "\r")

        f.write("]")

if __name__ == "__main__":
    file = readJsonFile()
    fileItems = getItems(file)
    sortItems(fileItems)
    writeFile(fileItems)
