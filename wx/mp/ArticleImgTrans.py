import json


def getArticleFile():
    with open(file='article/云南梅里雪山.md', mode='rt', encoding='utf-8') as f:
        data = f.readlines()
        return data


def getImgItems():
    with open('img/img_item.json') as f:
        data = f.read()
        return json.loads(data)


def replaceFileWithItems(articleFile, map):
    newArticleFile = []
    for aRow in articleFile:
        if aRow.__contains__('![[') and aRow[3:-3] in map:
            aRow = '![' + aRow[3:-3] + '](' + map[aRow[3:-3]] + ')\n'

        newArticleFile.append(aRow)
    return newArticleFile


def writeArticleFile(newArticleFile):
    with open(file='article/云南梅里雪山_out.md', mode='w', encoding='utf-8') as f:
        for aRow in newArticleFile:
            f.write(aRow)


def getNameImgItemMap(items):
    result = {}
    for item in items:
        result[item['name']] = item['cdn_url']

    return result


if __name__ == "__main__":
    articleFile = getArticleFile()
    items = getImgItems()
    itemMap = getNameImgItemMap(items)
    newArticleFile = replaceFileWithItems(articleFile, itemMap)
    writeArticleFile(newArticleFile)
