# -*- coding: utf-8 -*-

from jsonpath import jsonpath
import requests

from test_work_weixin_api_object.wework import WeWork


class Department(WeWork):
    """
    具体业务
    """

    # 创建部门
    def create_department(self, name, name_en, department_id):
        req = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "method": "POST",
            "params": {"access_token": self.token},
            "json": {
                "name": name,
                "name_en": name_en,
                "parentid": 1,
                "order": 1,
                "id": department_id
            }
        }
        r = self.send(req)
        return r.json()

    # 更新部门
    def update_department(self, department_id, name, en_name, parentid):
        req = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",
            "method": "POST",
            "json": {
                "id": department_id,
                "name": name,
                "name_en": en_name,
                "parentid": parentid,
                "order": 1}
        }
        r = self.send(req)
        return r.json()

    # 更新部门
    def delete_department(self, id):
        id = id
        # 使用字典保存URL以及method的信息，即接口的请求信息
        req = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}",
            "method": "GET"
        }
        r = self.send(req)
        return r.json()

    # 获取部门列表
    def get_department(self):
        req = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}",
            "method": "GET"
        }
        r = self.send(req)
        return r.json()
