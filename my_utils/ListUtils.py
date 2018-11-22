

def getNumberList(start_index=1, end_index=10, step=1):
    retlist = []
    for i in range(start_index, end_index, step):
        retlist.append(i)
    return retlist


def getNumberLists(start_index=1, end_index=1000, step=100):
    retlist = []
    for i in range(start_index, end_index, step):
        retlist.append(getNumberList(start_index, i, 1))
    return retlist
