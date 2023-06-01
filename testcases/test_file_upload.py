#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：project-xiaofang 
@File    ：test_file_upload
@IDE     ：PyCharm 
@Author  ：huangluo
@Date    ：2022/12/21 17:14 
@description :
'''
import re
import time

import pytest
import requests


class TestSendRequest:
    t = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 类变量通过类名访问
    token_login = ""
    token_headers = ""
    csrf_token = ""
    cks = ""
    session = requests.session()
    # def get_session(self):
    #
    #     session = requests.session()
    #     return session

    def test_get_token(self):
        # 发送post请求(data和json只需要传一个就可以，他们的区别）
        url = "http://120.46.140.183:8085/api/user/user/login"
        data = {
            # "code": "string",
            # "platform": "string",
            "password": 123456,
            "username": 15500000031
        }
        rep = TestSendRequest.session.request("post", url, json=data)
        # print(rep.json())
        TestSendRequest.token_login = rep.json()['data']['token']
        TestSendRequest.token_headers = {"token": TestSendRequest.token_login}
        print("这是登录token=", TestSendRequest.token_login)

    def test_success_upload(self):
        url = "http://120.46.140.183:8085/api/file/file/upload"
        data = {
            "media": open(r"C:\Users\huangluo\Desktop\车载测试课程彩页.pdf", "rb")
        }
        rep = requests.request("post", url, files=data, headers=TestSendRequest.token_headers)
        print(rep.json())

    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        rep = requests.request("get", url)
        # print(rep.text)

        # 通过正则表达式获取鉴权码
        TestSendRequest.csrf_token = re.search('name="csrf_token" value="(.*?)"', rep.text)[1]
        print(TestSendRequest.csrf_token)
        TestSendRequest.cks = rep.cookies

    # 需要到带请求头的接口
    def test_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username": "huangluo12",
            "password": "123456",
            "csrf_token": TestSendRequest.csrf_token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }

        headers = {
            "Accept": "application/json,test/javascript,/; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        rep = requests.request("post", url, data=data, headers=headers, cookies=TestSendRequest.cks)
        print(rep.json())


if __name__ == '__main__':
    pytest.main(["-vs"])
