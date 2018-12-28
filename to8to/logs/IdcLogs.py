def listErrorLogs():
    import requests

    url = "http://boss.we.com/logs/idc/elasticsearch/_msearch"

    # index = '{"index": ["log-java-idc-2018.12.27"], "ignore_unavailable": true, "preference": 1545975388333}'
    # query = '{"query":{"bool":{"must":[{"query_string":{"analyze_wildcard":true,"query":"*"}},{"match":{"proj":{"query":"t8t-scm-mdm","type":"phrase"}}},{"match":{"lv":{"query":"ERROR","type":"phrase"}}},{"range":{"@timestamp":{"gte":1545840000000,"lte":1545926399999,"format":"epoch_millis"}}}],"must_not":[]}},"size":3000,"sort":[{"@timestamp":{"order":"desc","unmapped_type":"boolean"}}],"_source":{"excludes":[]},"aggs":{"2":{"date_histogram":{"field":"@timestamp","interval":"30m","time_zone":"Asia/Shanghai","min_doc_count":1}}},"stored_fields":["*"],"script_fields":{},"docvalue_fields":["@timestamp"],"highlight":{"pre_tags":["@kibana-highlighted-field@"],"post_tags":["@/kibana-highlighted-field@"],"fields":{"*":{"highlight_query":{"bool":{"must":[{"query_string":{"analyze_wildcard":true,"query":"*","all_fields":true}},{"match":{"proj":{"query":"t8t-scm-mdm","type":"phrase"}}},{"match":{"lv":{"query":"ERROR","type":"phrase"}}},{"range":{"@timestamp":{"gte":1545840000000,"lte":1545926399999,"format":"epoch_millis"}}}],"must_not":[]}}}},"fragment_size":2147483647}}'
    payload = "{\"index\":[\"log-java-idc-2018.12.27\"],\"ignore_unavailable\":true," \
              "\"preference\":1545975388333}\r\n{\"query\":{\"bool\":{\"must\":[{\"query_string\":{" \
              "\"analyze_wildcard\":true,\"query\":\"*\"}},{\"match\":{\"proj\":{\"query\":\"t8t-scm-mdm\"," \
              "\"type\":\"phrase\"}}},{\"match\":{\"lv\":{\"query\":\"ERROR\",\"type\":\"phrase\"}}},{\"range\":{" \
              "\"@timestamp\":{\"gte\":1545840000000,\"lte\":1545926399999,\"format\":\"epoch_millis\"}}}]," \
              "\"must_not\":[{\"match\":{\"txt\":{\"query\":\"完成请求，200返回：\",\"type\":\"phrase\"}}}]}},\"size\":3000," \
              "\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{" \
              "\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"interval\":\"30m\"," \
              "\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{}," \
              "\"docvalue_fields\":[\"@timestamp\"],\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"]," \
              "\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{\"highlight_query\":{\"bool\":{" \
              "\"must\":[{\"query_string\":{\"analyze_wildcard\":true,\"query\":\"*\",\"all_fields\":true}}," \
              "{\"match\":{\"proj\":{\"query\":\"t8t-scm-mdm\",\"type\":\"phrase\"}}},{\"match\":{\"lv\":{" \
              "\"query\":\"ERROR\",\"type\":\"phrase\"}}},{\"range\":{\"@timestamp\":{\"gte\":1545840000000," \
              "\"lte\":1545926399999,\"format\":\"epoch_millis\"}}}],\"must_not\":[{\"match\":{\"txt\":{" \
              "\"query\":\"完成请求，200返回：\",\"type\":\"phrase\"}}}]}}}},\"fragment_size\":2147483647}}\r\n"\
        .encode("UTF-8")
    headers = {
        'authorization': "Basic ZGV2OnRlc3Q=",
        'kbn-version': "5.3.0-SNAPSHOT",
        'cache-control': "no-cache",
        "content-encoding": "gzip",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

if __name__ == "__main__":
    listErrorLogs()
