#!/usr/bin/python
# coding=utf-8

from urllib import request
import json


def signin(dict, cookie):
    host = dict["host"]
    if host:
        print(host)
        url = "http://" + dict["host"] + dict["url"]
        print(url)
        req = request.Request(url, method="POST")
        headers = dict["headers"]
        headers["Cookie"] = cookie
        req.headers = headers
        with request.urlopen(req) as f:
            try:
                bytes = f.read()
                print(type(bytes))
                print(str(bytes, encoding="utf-8"))
            except Exception as e:
                raise e


def signin_all():
    with open("./signin_template.json", 'r', encoding="utf-8") as load_f:
        template = json.load(load_f)
        with open("./user_cookies.json", 'r', encoding="utf-8") as users_f:
            users = json.load(users_f)
            for user in users:
                type = user['type']
                try:
                    signin(template[type], user["cookie"])
                except BaseException as e:
                    print(e)