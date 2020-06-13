import csv
import mysql.connector
import datetime

from mysql.connector import errorcode

config = {
    'host': '192.168.1.103',
    'user': 'root',
    'passwd': 'nicai123456',
    'port': 3306,
    'database': 'test',
    'charset': 'utf8'
}

# 需要查询的数据库表
databases_config = ['test']


class MyDBsDDLUtils:
    # db链接
    __dbConnection = None
    # 是否展示时间日志
    showTimeLog = False
    # 是否展示普通日志
    showLog = False

    def connect(self, myDatabase: str):
        try:
            config["database"] = myDatabase
            self.__dbConnection = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def close(self):
        if self.__dbConnection:
            self.__dbConnection.close()

    def query(self, sql: str):
        startTime = datetime.datetime.now().timestamp()
        if self.showTimeLog:
            print("startTime:", datetime.datetime.now().isoformat())
        cursor = self.__dbConnection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        endTime = datetime.datetime.now().timestamp()
        if self.showTimeLog:
            print("endTime:", datetime.datetime.now().isoformat())
            print("take time: ", endTime - startTime)
        if self.showLog:
            print("===== mysql query =====")
            print("[sql]")
            print(sql)
            print("[result]")
            print(result)
            print("===== mysql query end =====")
        return result

    def showAllTablesInDB(self):
        show_tables = "SHOW TABLES"
        return self.query(show_tables)

    def fetchAllFields(self, table):
        show_fields = "SHOW FULL FIELDS FROM " + table
        return self.query(show_fields)

    def getAllPathFields(self, myDatabase: str):
        if self.showLog:
            print(
                "====================================================================================================")
            print("database", myDatabase)
        self.connect(myDatabase)
        tables = self.showAllTablesInDB()
        tableAndFields = []
        for table in tables:
            fields = self.fetchAllFields(table[0])
            for field in fields:
                fullPathField = myDatabase + "." + table[0] + "." + field[0]
                fieldsJson = {
                    "fullPathField": fullPathField,
                    "Field": field[0],
                    "Type": field[1],
                    "Comment": field[8]
                }
                tableAndFields.append(fieldsJson)
        if self.showLog:
            print("tableAndFields", tableAndFields)
            print(
                "====================================================================================================")
        self.close()
        return tableAndFields

    @staticmethod
    def exportToExcel(result: list):
        with open("mydbsDDL_export.csv", "w", newline="") as csvFile:
            fieldnames = ["fullPathField", "Field", "Type", "Comment"]
            writer = csv.DictWriter(csvFile, fieldnames)
            writer.writeheader()
            writer.writerows(result)


# test
if __name__ == "__main__":
    result = []
    test = MyDBsDDLUtils()
    test.showLog = True
    for database in databases_config:
        result += test.getAllPathFields(database)
        test.exportToExcel(result)
    print("=========================Full Path About Field: yid, project_id=========================")
    print("full path", result)
    print("====================================================================================================")
