import glob
import re


# 思路来源：
# [找寻微信撤回的图片](https://zhuanlan.zhihu.com/p/21388706)
# [找寻微信撤回的图片（续）](https://zhuanlan.zhihu.com/p/21458386)
# 微信图片加密方式：通过将图片文件通过异或的方式保存为 .dat 文件
# 微信图片解密方式：找到对应固定表头，如下卖弄的xxA，XXB，就是固定的起始编码值，加解密出来结果即可。
# 逻辑程序参考：[PC端微信下的dat 文件在线解码还原成为图片](https://www.csdn.net/tags/ntjaeg0snjkwotitymxvzwo0o0oo0o0o.html)

# 解码逻辑
def decode_pc_dat(datFile):
    configs = [
        {"firstByte": 0xFF, 'secondByte': 0xD8, 'suffix': "jpg"},
        {"firstByte": 0x47, 'secondByte': 0x49, 'suffix': "gif"},
        {"firstByte": 0x89, 'secondByte': 0x50, 'suffix': "png"},
    ]

    with open(datFile, 'rb') as f:
        buf = bytearray(f.read())

    first = buf[0]
    second = buf[1]
    imgFile = datFile
    for config in configs:
        firstByte = config['firstByte']
        secondByte = config['secondByte']
        suffix = config['suffix']
        if firstByte ^ first ^ second == secondByte:  ## important
            magic = firstByte ^ first
            imgFile = re.sub(r'dat$', suffix, datFile)
            break

    with open(imgFile, 'wb') as f:
        f.write(bytearray(map(lambda b: b ^ magic, buf)))


# 获取指定目录下的，指定文件名
def getfileNamesByParentFilePath():
    # return os.path.dirname(scanFilePath)
    # listFilesName = Path(scanFilePath).rglob("**cofig")
    baseFilePath = "d:\Downloads\\tmp\\";

    listFilesName = []
    # print("path_project_name = " ,path_project_name)
    glob_glob = glob.glob(baseFilePath + "\\" + '**.dat', recursive=True)
    # print(glob_glob)
    listFilesName += glob_glob
    print("listFilesName = ", listFilesName)
    return listFilesName


if __name__ == '__main__':
    list = getfileNamesByParentFilePath()
    for aFile in list:
        decode_pc_dat(aFile)
