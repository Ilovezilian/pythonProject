import csv
import glob
import json
import os
from pathlib import Path


# 获取指定目录下的，指定文件名
def getfileNamesByParentFilePath():
    # return os.path.dirname(scanFilePath)
    # listFilesName = Path(scanFilePath).rglob("**cofig")
    baseFilePath = "d:\\shuaipanCompanyData\\developmentPartment\\2019\\spring cloud 升级\\task\\";
    # projectsName = ["dsp-ps-gdm", "t8t-scm-pda", "t8t-scm-exh", "t8t-scm-pom", "t8t-scm-fhc", "t8t-sys-dpt"] # shuai.pan使用
    projectsName = ["t8t-scm-ldm", "t8t-scm-sup", "t8t-scm-mrp", "t8t-scm-rem", "t8t-ps-odm"] # yilia.an使用
    projectsName = ["t8t-scm-oos"] # maxliu.liu使用

    listFilesName = []
    for projectName in projectsName:
        path_project_name = baseFilePath + projectName
        # print("path_project_name = " ,path_project_name)
        glob_glob = glob.glob(path_project_name + "\\" + '**/config', recursive=True)
        # print(glob_glob)
        listFilesName += glob_glob
    print("listFilesName = ", listFilesName)
    return listFilesName


## 获取文件中config内容
def getJsonObjectFromFilesPathAndName(filesPathAndName: list):
    autoTaskConfigJsonObjects = []
    for filePathAndName in filesPathAndName:
        with open(filePathAndName, encoding="utf8") as f:
            object = f.read()
            autoTaskConfigJsonObjects.append(json.loads(object))
            # autoTaskConfigJsonObjects.append(object)
            # print("object = ", object)

    print("autoTaskConfigJsonObjects = ", autoTaskConfigJsonObjects)
    return autoTaskConfigJsonObjects


## 组装参数，生成excel文档
def saveJsonObjectToExcel(jsonObjects: list):
    with open("autoTaskFile_maxliu.liu.csv", 'w', newline='') as csvFile:
        # csv.writer(csvFile, delimiter=' ', quotechar='|', quoing=csv.QUOTE_MINIMAL)
        fieldnames = ['jobName', 'description', 'cron', 'failover', 'jobProperties', 'monitorPort', 'jobType', 'shardingItemParameters', 'jobShardingStrategyClass', 'overwrite', 'shardingTotalCount', 'jobParameter', 'misfire', 'monitorExecution', 'maxTimeDiffSeconds', 'jobClass', 'disabled', 'streamingProcess']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jsonObjects)
    pass


if __name__ == "__main__":
    # 获取指定目录下的所有文件
    print(
        "start===========================================================================================================")
    filesPathAndName = getfileNamesByParentFilePath();
    # filesPathAndName = [
    #     'd:\\shuaipanCompanyData\\developmentPartment\\2019\\spring cloud 升级\\task\\dsp-ps-gdm\\annualFeeExpiredJob\\config']
    print("===========================================================================================================")
    autoTaskConfigJsonObjects = getJsonObjectFromFilesPathAndName(filesPathAndName)
    print("===========================================================================================================")
    saveJsonObjectToExcel(autoTaskConfigJsonObjects)
    print(
        "end===========================================================================================================")
