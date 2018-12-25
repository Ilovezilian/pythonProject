import time

import itchat

def sendFirstWXmsg():
    # 登录
    itchat.login()
    # 获取用户信息
    friends = itchat.get_friends()
    # 获取朋友信息
    for friend in friends:
        print(friend)
    # 发送消息
    for friend in friends:
        friend.send("嘿，" +friend.nickName+ "(^_^)：\n 今天每一朵雪花飘下，每一个烟火燃起，每一秒时间流动，都代表着要送你的一个平安祝福。\n--来自潘帅程序员python程序的祝福!突发奇想写了20行不到的代码群发一下祝福！")
        # print("嘿，" +friend.nickName+ "(^_^)：\n 今天每一朵雪花飘下，每一个烟火燃起，每一秒时间流动，都代表着要送你的一个平安祝福。\n--来自潘帅程序员python程序的祝福!突发奇想写了20行不到的代码群发一下祝福！")
        time.sleep(1)
    # 退出登录
    itchat.logout()
if __name__ == "__main__":
    sendFirstWXmsg()