import time

import itchat


def BeDeleteNumber():
    # 登录
    itchat.login()
    # 获取用户信息
    # friend = itchat.search_friends(name="潘帅")
    friends = itchat.get_friends()
    friend = friends[0]
    r = itchat.add_member_into_chatroom("tmpRoom", [friend]);
    if r['BaseResponse']['ErrMsg'] == '':
        status = r['MemberList'][0]['MemberStatus']
        itchat.delete_member_from_chatroom(friend['UserName'], [friend])
        return {3: u'该好友已经将你加入黑名单。',
                4: u'该好友已经将你删除。', }.get(status, u'该好友仍旧与你是好友关系。')


def BeDeleteNumbers():
    friends = itchat.get_friends()
    # 获取朋友信息

    for friend in friends:
        print(friend)
    # 发送消息
    for friend in friends:
        time.sleep(1)
    # 退出登录
    itchat.logout()


if __name__ == "__main__":
    BeDeleteNumber()
