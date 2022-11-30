# test
import datetime

from to8to.t8t_scm_mdm.mdm_mysql import MDMMySql

if __name__ == "__main__":
    test = MDMMySql()
    test.connect()

    for i in range(18):
        queryGoodsSql = "select id from supply_goods limit 0," + str(100 * (i+1))
        result = test.query(queryGoodsSql, False)
        ids = ""
        for row in result:
            if ids.__len__() != 0:
                ids += ", "
            ids += str(row['id'])
        # print(ids.__sizeof__())
        sql = "SELECT goods.id AS id,goods.sku_id AS skuId,goods.goods_name AS goodsName,goods.goods_code AS goodsCode, goods.enterprise_code AS enterpriseCode,goods.brand_id AS brandId,goods.goods_group AS goodsGroup, goods.goods_imgs AS goodsImgs,goods.mnemonic_code AS mnemonicCode, ext.model,ext.standard,ext.goods_category AS goodsCategory,ext.basic_unit AS basicUnit, ext.style,ext.origin,ext.material,ext.color,ext.tax_rate AS taxRate, ext.green_level AS greenLevel,ext.technique ,ext.category_pro_vals AS categoryProVals,ext.normative " \
              "FROM supply_goods AS goods LEFT JOIN supply_goods_ext AS ext ON goods.id =ext.id " \
              "WHERE goods.id IN (" + str(ids) + ")"
        print("result.size = ", result.__len__() , sql)
        startTime = datetime.datetime.now().timestamp()
        result = test.query(sql, False)
        endTime = datetime.datetime.now().timestamp()
        print("endTime:", datetime.datetime.now().isoformat())
        print("take time: ", endTime - startTime)
        print()

    # result = test.clear_mdm_shop_info()
    # result = test.doDelete("mdm_appointment_info", "real_shop_id")
    # print(result)
    # test.clear_all()
