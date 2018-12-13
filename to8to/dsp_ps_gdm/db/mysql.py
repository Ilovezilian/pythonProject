import mysql.connector
import datetime

from mysql.connector import errorcode

config = {
    'host': "192.168.1.121",
    'user': "hongfeng.huang",
    'passwd': "741852@hhf",
    'port': 3306,
    'database': 'dsp_ps_gdm',
    'charset': 'utf8'
}


class GDMMySql:
    __dbConnection = None

    def connect(self):
        try:
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

    def query(self, sql, showLog=False):
        startTime = datetime.datetime.now().timestamp()
        print("startTime:", datetime.datetime.now().isoformat())
        cursor = self.__dbConnection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        endTime = datetime.datetime.now().timestamp()
        print("endTime:", datetime.datetime.now().isoformat())
        print("take time: ", endTime - startTime)
        if showLog:
            print("===== mysql query =====")
            print("[sql]")
            print(sql)
            print("[result]")
            print(result)
            print("===== mysql query end =====")
        return result

    def testQuery(self):
        sql1 = "SELECT o.order_code AS orderCode, o.owner_name AS ownerName, o.owner_phone_id AS ownerPhoneId, " \
               "o.receive_name AS receiveName, o.receive_phone_id AS receivePhoneId, o.receive_address AS " \
               "receiveAddress, o.goods_demand_time AS goodsDemandTime, o.project_id AS projectId, " \
               "o.source_project_id AS sourceProjectId, o.create_time AS createTime, o.consignee_time AS " \
               "consigneeTime, o.remark AS orderRemark, i.goods_id AS goodsId, i.goods_source AS goodsSource, " \
               "i.remark AS itemRemark,i.sales_goods_demand_amount AS salesGoodsDemandAmount,i.sales_unit AS " \
               "salesUnit, i.sales_unit_price AS salesUnitPrice, i.sales_company_unit_price AS salesCompanyUnitPrice," \
               "i.order_item_status AS orderItemStatus, i.remark AS itemRemark " \
               "FROM gdm_pmat_order o LEFT JOIN gdm_pmat_order_item i ON o.order_code = i.goods_demand_code " \
               "WHERE o.root_org_id = '580' AND o.order_source IN ( 8 , 9 , 10 , 11 ) AND o.create_time BETWEEN 1535731200 AND 1541001600 " \
               "ORDER BY o.create_time DESC"
        self.query(sql1)

        sql2 = "SELECT o.order_code AS orderCode, o.owner_name AS ownerName, o.owner_phone_id AS ownerPhoneId, " \
               "o.receive_name AS receiveName, o.receive_phone_id AS receivePhoneId, o.receive_address AS " \
               "receiveAddress, o.goods_demand_time AS goodsDemandTime, o.project_id AS projectId, " \
               "o.source_project_id AS sourceProjectId, o.create_time AS createTime, o.consignee_time AS " \
               "consigneeTime, o.remark AS orderRemark, i.goods_id AS goodsId, i.goods_source AS goodsSource, " \
               "i.remark AS itemRemark,i.sales_goods_demand_amount AS salesGoodsDemandAmount,i.sales_unit AS " \
               "salesUnit, i.sales_unit_price AS salesUnitPrice, i.sales_company_unit_price AS " \
               "salesCompanyUnitPrice, i.order_item_status AS orderItemStatus, i.remark AS itemRemark " \
               "FROM gdm_pmat_order o LEFT JOIN gdm_pmat_order_item i ON o.order_code = i.goods_demand_code " \
               "WHERE o.root_org_id = '580'AND o.create_time BETWEEN 1535731200 AND 1541001600  AND o.order_source IN ( 8 , 9 , 10 , 11 )" \
               "ORDER BY o.create_time DESC"
        self.query(sql2)


# test
if __name__ == "__main__":
    test = GDMMySql()
    test.connect()
    for i in range(10):
        test.testQuery()
        print("heihei", i, "time")
    test.close()
