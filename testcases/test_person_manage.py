#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：project-xiaofang 
@File    ：test_person_manage
@IDE     ：PyCharm 
@Author  ：huangluo
@Date    ：2022/11/25 10:54 
@description :管理员人员管理
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

    def test_adduser(self):
        url = "http://120.46.140.183:8085/api/user/personManage/addUserInfo"
        data = [
            {

                "birth": "1995-01-01 00:00:00",
                "classId": "",
                "clientUnitId": "",
                "dutiesName": "",
                "emergencyName": "紧急联系人002",
                "emergencyPhone": "15545354649",
                "gender": "男",
                "height": "185",
                "name": "用户001",
                "organizationId": "",
                "relation": "关系001",
                "roleIds": "20",
                "startDate": "",
                "telephone": "15512346697",
                type: "1",
                "userIcon": "",
                "weight": "80"
            }
        ]
        headers = {"token": TestSendRequest.token_login}
        # headers = TestSendRequest.token_headers
        rep = requests.post(url, json=data, headers=headers)
        print(rep.json())


if __name__ == '__main__':
    pytest.main(["-vs"])
