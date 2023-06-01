#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：project-xiaofang 
@File    ：add_organization
@IDE     ：PyCharm 
@Author  ：huangluo
@Date    ：2022/11/18 11:23 
@description :
'''
import time

import pytest
import requests


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

    # 添加班组
    def test_add_organization_success(self):
        url = "http://120.46.140.183:8085/api/user/organization/addOrganization"
        data = [{
            "organizationLeader":
                "",
            "organizationName": "班名称" + TestSendRequest.t,
            "parentId": 549,
            "userIds": []
        }]
        rep = requests.post(url, json=data, headers=TestSendRequest.token_headers)
        print(rep.json())


i = 0
while i <= 10:
    if __name__ == '__main__':
        pytest.main(["-vs"])
    i = i + 1
