# -*- coding: utf-8 -*-

from test_work_weixin_tag_ao.wework import WeWork


class Tag(WeWork):
    """
    具体业务
    """

    # 创建标签
    def create_tag(self, tagname, tagid):
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
            "json": {
                "tagname": tagname,
                "tagid": tagid
            }
        }
        r = self.send(req)
        return r

    # 更新标签
    def update_tag(self, tagid, tagname):
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
            "json": {
                "tagid": tagid,
                "tagname": tagname
            }
        }
        r = self.send(req)
        return r.json()

    # 删除标签
    def delete_tag(self, tagid):
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}",
            "params": {"tagid": tagid}
        }
        r = self.send(req)
        return r.json()

    # 获取标签成员
    def get_tag_user(self, tagid):
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}",
            "params": {"tagid": tagid}
        }
        r = self.send(req)
        return r.json()

    # 增加标签成员
    def create_tag_user(self, tagid, userlist: list, partylist: list):
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}",
            "json": {"tagid": tagid,
                     "userlist": userlist,
                     "partylist": partylist
                     }
        }
        r = self.send(req)
        return r.json()

    # 删除标签成员
    def delete_tag_user(self, tagid, userlist: list, partylist: list):
        req = {
            "method": "POST",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}",
            "json": {"tagid": tagid,
                     "userlist": userlist,
                     "partylist": partylist
                     }
        }
        r = self.send(req)
        return r.json()

    # 获取标签列表
    def get_tag_list(self):
        req = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        }
        r = self.send(req)
        return r.json()
