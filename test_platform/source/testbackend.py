# -*- coding:utf-8 -*-
# @time    :2021/7/17 13:44
# @Author  :dmingzhu
# @dmingzhu:testbackend.py
# -*- coding:utf-8 -*-
# @time    :2021/7/17 12:23
# @Author  :dmingzhu
# @dmingzhu:bb.py
import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins
from flask_cors import CORS

app=Flask(__name__)
# 使用CORS
CORS(app)

# 用flask_restful创建新的api
api = Api(app)
# 在配置文件指定数据库uri   用户名：密码@pi:port/库名
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123456@192.168.99.100:3306/test_platform"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.99.100:3306/test_platform'
# 添加jenkins配置到app
app.config["jenkins"]=Jenkins(
        baseurl="http://192.168.99.100:8080/",
        username="admin",
        password="123"
    )

# 初始化数据库
db = SQLAlchemy(app)

# 设计用于存放测试用例的数据库表结构
# 假设一个测试用例关联多个测试任务

class Case(db.Model):
    "设计表字段"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    steps = db.Column(db.String(100))

    def __repr__(self):
        return '<Case %r>' % self.name


# 设计测试任务数据库结构
class Task(db.Model):
    "设计表字段"
    id = db.Column(db.Integer, primary_key=True)
    # 在task表中确定外键
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'))
    # 建立关系case和task
    case = db.relationship('Case', backref=db.backref('task', lazy=True))
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))

    def __repr__(self):
        return '<Task %r>' % self.name



class TestCaseService(Resource):
    """
    创建测试用例服务
    id为None或不在列表中，返回全部
    id存在则返回正确记录
    """
    def get(self):
        """
        测试用例浏览获取
        /testcase.json   获取全部用例
        /testcase.json?id=1 获取id=1的用例
        """
        id = request.args.get("id")
        print(id)
        # id = request.json.get("id")
        ids = [testcase_id.id for testcase_id in Case.query.all()]
        # print(ids)


        if id is None or int(id) not in ids:
            # print("不在id列表")
            testcases = Case.query.all()
            # print(testcases)
            res = [{
                "id":case.id,
                "name":case.name,
                "description":case.description,
                "steps":json.loads(case.steps)
            } for case in testcases]
            print(res)
            return {
                "body":res
            }
        else:
            # print("在id列表")
            testcase = Case.query.filter_by(id=id).first()
            # print(type(testcase))
            res = {
                "id":testcase.id,
                "name":testcase.name,
                "description":testcase.description,
                "steps":testcase.steps
            }
            return {
                "body":res
            }


    def post(self):
        """
        测试用例上传，更新
        /testcase.json {"name":"", "description":"", "steps":[],}
        request.json   从flask.json导入
        """
        app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

        id = request.args.get("id")
        if id:
            # 更新
            testcase = Case.query.filter_by(id=id).first()
            testcase.name = request.json.get("name"),
            testcase.description = request.json.get("description")
            testcase.steps = json.dumps(request.json.get("steps"))

        else:
            #新建
            # 从请求的json中get对应的值，并存入到数据库相应字段
            testcase = Case(
                # id = request.json.get("id"),
                name = request.json.get("name"),
                description = request.json.get("description"),
                # 转成json
                steps = json.dumps(request.json.get("steps"))
            )

            # 在与数据建立的连接上追加记录
            db.session.add(testcase)
        # 提交
        db.session.commit()
        testcases = Case.query.all()
        res = [{
            "id":case.id,
            "name":case.name,
            "description":case.description,
            "steps":json.loads(case.steps)
        } for case in testcases]

        return {
            "msg":"testcase update ok!",
            "body":res
        }

#     删除服务
    def delete(self):
        id = request.json.get("id")
        print(id)
        task_case_ids = [task_case.case_id for task_case in Task.query.all()]
        print(task_case_ids)
        if int(id) in task_case_ids:
            print("用例已关联任务，不能删除！")
            return {
                "msg":"用例已关联任务，不能删除！"
            }
        else:
            testcase = Case.query.filter_by(id=id).first()
            # 将删除对象传递到db.session
            db.session.delete(testcase)
            db.session.commit()
            return {
                "msg":"delete succes"
            }

class TestTaskService(Resource):
    """
    创建测试任务服务
    """
    # 查看
    def get(self):
        # 从url中获取参数id
        id = int(request.args.get("id"))
        # print(type(id))
        # print(id)
        tasks = Task.query.all()
        ids = [task.id for task in tasks]
        # print(ids)
        # list成员运算时，注意判断两者的数据类型
        if id not in ids:
            print("start")
            res = []
            for task in tasks:
                res.append({"case_id":task.case_id,
                            "name":task.name,
                            "description":task.description})
            return {
                "msg":"ok",
                "body":res
            }
        else:
            this_task = Task.query.filter_by(id=id).first()
            return {
                "msg": "ok",
                "body": {
                    "case_id": this_task.case_id,
                    "name": this_task.name,
                    "description": this_task.description
                }
            }


    # 插入
    def post(self):
        # print(request.json)
        # 可以用json获取对应参数，因为在测试代码中post传参用的json
        tasks = Task(
            id = request.json.get("id"),
            case_id = request.json.get("case_id"),
            name = request.json.get("name"),
            description = request.json.get("description")
        )

        db.session.add(tasks)
        db.session.commit()
        print("task update ok")

    def put(self):
        id = request.json.get("id")
        print(id)
        if id:
            task =Task.query.filter_by(id = id).first()
            print(task.name)
            case_id = task.case_id
            case = Case.query.filter_by(id=case_id).first()
            print(case.name)
            print(case.steps)
            jenkins_server = app.config["jenkins"]
            jobs = jenkins_server.keys()
            jenkins_server.build_job("testplatform_0729", {"testcase": case.name})
            # print(res)
            # job = jenkins_server['testplatform_0729']
            # job.invoke({"case_id":"test data"})
        return jobs

class TestReportService(Resource):
    """
    创建测试报告服务
    回传jenkins用例执行结果
    """
    def get(self):

        return "get request for report"

    def post(self):

        pass


# 用api.add_resource(类名， 路由)给资源追加路由关系
api.add_resource(TestCaseService, "/testcase")
api.add_resource(TestTaskService, "/testtask")
api.add_resource(TestReportService, "/testreport")



if __name__ == '__main__':
    app.run(debug=True)