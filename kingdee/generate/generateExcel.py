import csv
import json


def fetchFromJsonFile():
    with open('attendanceFileListResult.json', 'rb') as f:
        data = f.read()
        loads = json.loads(data)
        return loads["rows"]


def getPersonsFromFileData(dataFromFile: list):
    persons = []
    for item in dataFromFile:
        persons.append({"number": item["person.number"], "name": item["person.name"]})
    return persons


def generateDataFromPersons(persons: list):
    excelData = []
    for aPerson in persons:
        for aMonth in range(1, 12):
            for aDay in range(1, 30):
                excelData.append({
                    "number": aPerson["number"],
                    "name": aPerson["name"],
                    "date": "2021-" + str(aMonth) + "-" + str(aDay),
                    "time": "08:00",
                    "reason": "忘记打卡",
                    "remark": "备注"
                })
    return excelData


def outputCSVExcel(excelData: list):
    with open("fillSignCardImport_export.csv", "w", newline="") as csvFile:
        fieldnames = ["number", "name", "date", "time", "reason", "remark"]
        writer = csv.DictWriter(csvFile, fieldnames)
        writer.writeheader()
        writer.writerows(excelData)


if __name__ == '__main__':
    dataFromFile = fetchFromJsonFile()
    persons = getPersonsFromFileData(dataFromFile)
    excelData = generateDataFromPersons(persons)
    print(excelData.__len__())
    outputCSVExcel(excelData)
