import requests


class Tag:
    def __init__(self):
        self.token = ""

    def get_token(self):
        """
        获取token
        :param corpid:
        :param corpsecret:
        :param url:
        :return:
        """
        corpid = "ww69694e10de384523"
        corpsecret = "_yb7L6V2q0Guqk44vdR9jm9HYIzc5aqiuKNKeo3muFI"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        # requests.adapters.DEFAULT_RETRIES = 5
        # s = requests.session()
        # s.keep_alive = False
        r = requests.get(url=url, params=param, proxies=proxies, verify = False)
        # print(r.json())
        # print(r.json()["access_token"])
        self.token = r.json()["access_token"]
        return self.token, self

    def list(self):
        """
        获取企业标签列表
        若tag_id和group_id均为空，则返回所有标签
        同时传递tag_id和group_id时，忽略tag_id，仅以group_id作为过滤条件
        :return:
        """
        param = {
            "access_token": self.token
        }
        json = {
            "tag_id": [],
            "group_id": []
        }
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list", params=param,
                          json=json,
                          proxies =proxies,
                          verify = False
                          )
        # return json.dumps(r.json(), indent=2)
        return r

    def add(self, group_name, tag_name_list):
        """
        添加企业客户标签，每个企业最多可 添加3000个企业标签
        access_token ： 调用接口的凭证
        tag.name：必填,添加的标签名称，最长为30个字符
        group_name：标签组名称，最长30个字符
        tag.order：标签次序，值越大，越靠前
        :return:
        """
        param = {
            "access_token":self.token
        }
        json = {
            "group_name" : group_name,
            "tag" : tag_name_list
        }
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params=param,
                          json=json,
                          proxies = proxies,
                          verify=False)

        return r

    def delete(self, tag_ids=None, group_ids=None):
        """
        删除标签
        tag_id和group_id不能同时为空
        如果一个标签组下所有的标签均被删除，则标签组会被自动删除。
        :return:
        """
        param = {
            "access_token":self.token
        }
        json = {
            "tag_id": tag_ids,
            "group_id": group_ids
        }
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                          params=param,
                          json=json,
                          proxies=proxies,
                          verify=False)

        return r

    def clear_all(self):
        group_ids = []
        r = self.list()
        list_group = r.json()["tag_group"]
        # print(list_group)
        for group in list_group:
            # print(group)
            if "group_id" in group:
                group_ids.append(group["group_id"])
        # print(group_ids)
        self.delete(group_ids=group_ids)
        list_end = self.list()
        return list_end

    def edit(self, old_group_name, new_group_name):
        """
        编辑
        access_token 调用凭证
        id 必填，标签或标组的id
        name id对应的新name

        标签组不能重名
        同一标签组的标签不能重名
        :return:
        """
        group_id = ""
        group_name = ""
        list = self.list()
        # print(list.json())
        for tag in list.json()["tag_group"]:
            # print(tag)
            if tag["group_name"] == old_group_name:
                group_name = new_group_name
                group_id = tag["group_id"]
                # print(group_id)
        param = {
            "access_token":self.token
        }
        json = {
            "id" : group_id,
            "name" : group_name
        }
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                          params = param,
                          json = json,
                          proxies = proxies,
                          verify = False)
        edit_list = self.list()
        return edit_list, group_id