import json


def listProjects(projectIds):
    import http.client

    conn = http.client.HTTPConnection("192.168.1.172:40001")

    payload = {
        "args": {
            "search": {
                "sourceProjectId_in": projectIds
            },
            "fields": [
                "id",
                "sourceProjectId",
                "orgId",
                "rootOrgId",
                "ownerId",
                "ownerName",
                "appellation",
                "isPrimary",
                "projectSource",
                "chiefDesignerId",
                "designerId",
                "orderMainStatus",
                "orderSubStatus",
                "realSignedTime",
                "startTime",
                "preferStyleId",
                "expectDecorateTime",
                "houseAddress",
                "houseType",
                "houseStyle",
                "houseArea",
                "houseValuationArea",
                "estateId",
                "estateName",
                "cityId",
                "townId",
                "decoratePattern"
            ],
            "sort": [
            ],
            "page": 1,
            "size": 100
        }
    }

    headers = {
        's': "/biz/dsp-prs-mdm/app",
        'm': "views.decorationOrder.queryDetailPage",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "76767914-7a8f-68e3-17a1-bacf4c564632"
    }

    conn.request("POST", "/", payload.__str__(), headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


def getProjects():
    import http.client

    conn = http.client.HTTPConnection("192.168.1.172:40001")

    payload = "{\r\n    \"args\":{\"size\":20,\"searchParam\":{},\"page\":1}\r\n}   "

    headers = {
        # 'content-type': "application/json",
        's': "/biz/dsp-ps-gdm/app",
        'm': "views.goodsDemand.queryProjectPageWeb2",
        'rpc-rootOrgId': 162388,
        'rpc-uid': 112776,
        'rpc-saas-dataperm': "[ { 'tableName': 'ass_assign_principal', 'field': 'root_org_id' }, { 'tableName': 'hmm_measure_appoint', 'field': 'root_org_id' }, { 'tableName': 'hmm_measure_order', 'field': 'root_org_id' }, { 'tableName': 'hmm_measure_picture', 'field': 'root_org_id' }, { 'tableName': 'hmm_measure_punch', 'field': 'root_org_id' }, { 'tableName': 'mdm_decoration_order', 'field': 'root_org_id' }, { 'tableName': 'mdm_decoration_order_contact', 'field': 'root_org_id' }, { 'tableName': 'mdm_decoration_order_ext', 'field': 'root_org_id' }, { 'tableName': 'mdm_decoration_order_house', 'field': 'root_org_id' }, { 'tableName': 'mdm_decoration_order_record', 'field': 'root_org_id' }, { 'tableName': 'mdm_decoration_order_status_track', 'field': 'root_org_id' }, { 'tableName': 'gdm_goods_demand', 'field': 'root_org_id' }, { 'tableName': 'gdm_goods_demand_cache', 'field': 'root_org_id' }, { 'tableName': 'gdm_goods_demand_item', 'field': 'root_org_id' }, { 'tableName': 'gdm_goods_demand_item_config', 'field': 'root_org_id' }, { 'tableName': 'gdm_goods_demand_verify_record', 'field': 'root_org_id' }, { 'tableName': 'pmd_attach', 'field': 'root_org_id' }, { 'tableName': 'psm_project_node_modify_record', 'field': 'root_org_id' }, { 'tableName': 'psm_project_node_property', 'field': 'root_org_id' }, { 'tableName': 'psm_project_node_relation', 'field': 'root_org_id' }, { 'tableName': 'psm_project_schedule_node', 'field': 'root_org_id' }, { 'tableName': 'qcm_platform_check', 'field': 'root_org_id' }]",
        'cache-control': "no-cache",
        # 'postman-token': "767cfd12-29e2-77ad-7e99-3c3d2dacb020"
    }

    conn.request("POST", "/", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


if __name__ == "__main__":
    res = json.loads(getProjects())
    # print(res)
    projectIds = []
    for project in res['result']["rows"]:
        projectIds.append(project["sourceProjectId"])

    # print(projectIds)
    for id in projectIds:
        result = json.loads(listProjects([id]))
        print(result['result']["total"])
        if result['result']["total"] > 1:
            print(id)

    # projects = json.loads(listProjects(projectIds))
    # # map = {}
    # for project in res['result']["rows"]:
    #     print(project)
    #     pass
    #     # if project




