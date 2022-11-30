import mysql.connector

config = {
    'host': "192.168.1.121",
    'user':"hongfeng.huang",
    'passwd':"741852@hhf",
    'port': 3306,
    'database': 't8t_scm_mdm',
    'charset': 'utf8'
}

class MDMMySql:
    __dbConnection = None

    def connect(self):
        self.__dbConnection = mysql.connector.connect(**config)

    def close(self):
        if self.__dbConnection:
            self.__dbConnection.close()

    def query(self, sql, showLog = True):
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
        self.__doDelete("mdm_appointment_info")
        #self.__doDelete("mdm_appraise")
        #self.__doDelete("mdm_appraise_tag")
        self.__doDelete("mdm_brokerage_info")
        self.__doDelete("mdm_collected_shop")
        self.__doDelete("mdm_coupon")
        self.__doDelete("mdm_coupon_receive")
        #self.__doDelete("mdm_designer")
        self.__doDelete("mdm_dispatch_config")
        #self.__doDelete("mdm_dispatch_order")
        #self.__doDelete("mdm_dispatch_record")
        self.__doDelete("mdm_dispatch_type")
        self.__doDelete("mdm_goods")
        #self.__doDelete("mdm_goods_desc")
        self.__doDelete("mdm_msg_push_record")
        #self.__doDelete("mdm_page_config")

        #删除所有回复，回复中shop_id为0，TODO:这里shop_id也不应该为0
        results = self.query("select id from mdm_question_answer where shop_id IN(" + self.__get_shop_ids() + ")", False)
        ids = []
        for result in results:
            ids.append(str(result['id']))
        if len(ids) > 0:
            splitString = ','
            idsString = splitString.join(ids)
            self.__delete("DELETE FROM mdm_question_answer WHERE parent_id IN(" + idsString + ")")
        
        self.__doDelete("mdm_question_answer")
        self.__doDelete("mdm_shared_click")
        self.__doDelete("mdm_shared_shop")
        self.__doDelete("mdm_shop_desc")
        self.__doDelete("mdm_shop_info")
        self.__doDelete("mdm_shop_pic")
        self.__doDelete("mdm_shop_service")
        #self.__doDelete("mdm_shop_settled")
        self.__doDelete("mdm_store_case", "store_id")
        #self.__doDelete("mdm_withdraw_info")

    def __doDelete(self, table, column = 'shop_id'):
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

#test
if __name__ == "__main__":
    test = MDMMySql()
    test.connect()
    #result = test.query("select * from mdm_shop_info")
    #result = test.clear_mdm_shop_info()
    #result = test.doDelete("mdm_appointment_info", "real_shop_id")
    #print(result)
    # test.clear_all()