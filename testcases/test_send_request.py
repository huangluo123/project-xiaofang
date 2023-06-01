# -*- coding:utf8 -*- #
# ----------------------------------------------------------------------------------------------------------------------
# ProjectName:project-xiaofang
# FileName:   test_send_request.py
# Author:     huangluo  
# Datetime:   2022/11/13  21:18
# Description:
# ----------------------------------------------------------------------------------------------------------------------
import time

import pytest
import requests


# rep = requests.request()
# # 返回字符串的数据
# print(rep.text)
# # 返回字节格式的数据
# print(rep.content)
# # 返回字典格式的数据
# print(rep.json())
# # 状态码
# print(rep.status_code)
# # 返回状态信息
# print(rep.reason)
# # 返回cookies信息
# print(rep.cookies)
# # 返回一个编码格式
# print(rep.encoding)
# # 返回它的响应头
# print(rep.headers)


class TestSendRequest:
    t = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 类变量通过类名访问
    token_login = ""
    token_headers = ""

    def test_get_token(self):
        # 发送post请求(data和json只需要传一个就可以，他们的区别）
        url = "http://120.46.140.183:8085/api/user/user/login"
        data = {
            # "code": "string",
            # "platform": "string",
            "password": 123456,
            "username": 15500000000
        }
        rep = requests.post(url, json=data)
        # print(rep.json())
        TestSendRequest.token_login = rep.json()['data']['token']
        TestSendRequest.token_headers = {"token": TestSendRequest.token_login}
        print("这是登录token=", TestSendRequest.token_login)

    def test_client_unit(self):
        # 获取所有客户单位信息
        # 发送get请求方法
        url = "http://120.46.140.183:8085/api/user/organization/getByParent?id=253&keyword="
        data = {
            "id": "253",
            "keyword": ""
        }

        headers = {"token": TestSendRequest.token_login}
        rep = requests.get(url, params=data, headers=headers)
        print(rep.json())

    # get 请求
    def test_personmanage_getadmin(self):
        url = "http://120.46.140.183:8085/api/user/personManage/getAdmin"
        data = {

        }
        headers = {"token": TestSendRequest.token_login}
        rep = requests.get(url, params=data, headers=headers)
        print(rep.json())

    # 添加消防单位
    def test_add_organization(self):
        url = "http://120.46.140.183:8085/api/user/organization/addOrganization"
        data = [{
            "organizationAddress": "地址" + TestSendRequest.t,
            "organizationName": "名称" + TestSendRequest.t,
            "organizationPerson": "消防联系人" + TestSendRequest.t,
            "organizationPhone": "15" + TestSendRequest.t[5:],
            "parentId": 253
        }]
        headers = {"token": TestSendRequest.token_login}
        rep = requests.post(url, json=data, headers=headers)
        print("添加消防单位", rep.json())
        # 实际的结果
        actual = rep.json()["code"]
        print(actual)
        # 预期结果
        expected = "200"
        # 断言
        # self.assertEqual(expected, actual)
        # time.sleep(1)

    # 添加客户单位
    def test_add_clientunit(self):
        url = "http://120.46.140.183:8085/api/user/clientUnit/add"
        data = [{
            "clientUnitAddress": "客户单位地址" + TestSendRequest.t,
            "clientUnitContact": "联系人" + TestSendRequest.t,
            "clientUnitId": 0,
            "clientUnitInfo": TestSendRequest.t[:8],
            "clientUnitName": "客户单位名称" + TestSendRequest.t[:6],
            "clientUnitTel": "155" + TestSendRequest.t[6:]
        }]

        rep = requests.post(url, json=data, headers=TestSendRequest.token_headers)
        print(rep.json())
        print(TestSendRequest.t)
        # time.sleep(1)


i = 0
while i <= 10:
    if __name__ == '__main__':
        pytest.main(["-vs"])
    i = i + 1
