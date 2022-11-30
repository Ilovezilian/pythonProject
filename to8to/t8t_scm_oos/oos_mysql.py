import mysql.connector

config = {
    'host': "192.168.1.121",
    'user': "hongfeng.huang",
    'passwd': "741852@hhf",
    'port': 3306,
    'database': 't8t_scm_oos',
    'charset': 'utf8'
}


class OOSMySql:
    __dbConnection = None

    def connect(self):
        self.__dbConnection = mysql.connector.connect(**config)

    def close(self):
        if self.__dbConnection:
            self.__dbConnection.close()

    def query(self, sql, showLog=True):
        cursor = self.__dbConnection.cursor(dictionary=True)
        self.__dbConnection.commit()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        if showLog:
            print("===== mysql query =====")
            print("[sql]")
            print(sql)
            print("[result]")
            print(result)
            print("===== mysql query end =====")

        return result

    def clear_all(self):
        pass

    def __doDelete(self, table, column='shop_id'):
        sql = "DELETE FROM " + table + " WHERE " + column + " IN(" + self.__get_shop_ids() + ")"
        return self.__delete(sql)

    def __delete(self, sql):
        cursor = self.__dbConnection.cursor()
        cursor.execute(sql)
        count = cursor.rowcount
        self.__dbConnection.commit()
        cursor.close()
        return count

    # def __get_shop_ids(self):
    #     return str(MAIN_SHOP['shopId']) + "," + str(DIRECT_BRANCH_SHOP['shopId']) + "," + str(PARTNER_BRANCH_SHOP['shopId'])
    def get_shop_ids(self):
        sql = 'select shop_id from oos_coupon group by shop_id'
        res = list()
        for item in self.query(sql, False):
            res.append(item['shop_id'])
        return res


# test
if __name__ == "__main__":
    test = OOSMySql()
    test.connect()
    print(test.get_shop_ids())
    # result = test.query("select * from mdm_shop_info")
    # result = test.clear_mdm_shop_info()
    # result = test.doDelete("mdm_appointment_info", "real_shop_id")
    # print(result)
    # test.clear_all()
