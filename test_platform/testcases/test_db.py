import json

from jenkinsapi.jenkins import Jenkins

from test_platform.source.testbackend import db

def test_creat_table():
    db.create_all()

def test_jenkins():
    server=Jenkins(
        baseurl="http://192.168.99.100:8080/",
        username="admin",
        password="123"
    )
    print(server.keys())
    print(server['testplatform_0729'])
    res =server.build_job("testplatform_0729", {"case_id":"test data"})
    # print("打印参数列表",server["testplatform_0729"].get_params_list())
    # print("get build by params",jenkins_job["testplatform_0729"].get_build_by_params({"case_id":"test data"}))
    #
    # res = server['testplatform_0729'].invoke({"case_id":"test data"})
    print(res)
