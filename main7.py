# This is a sample Python script.


# 这是单行注释
"""
这是多行注释
这是多行注释
"""
import json

import requests as requests

'''
也可以用三个单引号来进行多行注释
'''
import _thread
import time

if __name__ == '__main__':
    dataset_name_id = {}
    REQUEST_HEADERS = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    url = "http://172.25.33.105:8082" + "/permission/listUserDatasets?userid=" + str(1348092268)
    res = requests.get(url, headers=REQUEST_HEADERS)
    tables = json.loads(res.text)['data']
    print(tables)

    if not tables:
        print("111")
    else:
        print("222")

    for table in tables:
        uniq_name = table['datasetSchema'] + "_" + table['datasetName']
        dataset_name_id[uniq_name] = table['datasetId']

    print(dataset_name_id)
