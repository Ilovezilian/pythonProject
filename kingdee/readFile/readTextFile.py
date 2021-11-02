if __name__ == '__main__':
    with open("rows.txt", "rb") as f:
        rows = f.readlines()

    # rows = data.decode("utf-8")
    a = set()
    res = ""
    for aRowStr in rows:
        aRow = aRowStr.decode("utf-8").strip()
        if a.__contains__(aRow):
            res += aRow + "\n"
        else:
            a.add(aRow)

    # print(res)
    with open("repeatRows.txt", "w") as f:
        f.write(res)
