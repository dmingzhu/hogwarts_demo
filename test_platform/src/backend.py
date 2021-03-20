
# -*- coding:utf-8 -*-
# @time    :2021/1/6 21:01
# @Author  :dmingzhu
# @dmingzhu:backend.py
import json

from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return "Welcome to my test platform!!"

# sqlalchemy连mysql
# pymsql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://用户名:密码@域名或ip:端口/数据库'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@192.168.99.100:3306/testPlatform'

app.config['jenkins'] = Jenkins(
        "http://192.168.99.100:8080/",
        username="admin",
        password="6a9eb15459dc48de87c0acee229847ac"
    )



# 初始化SQLAlchemy
db = SQLAlchemy(app)

# 定义testcase表结构
class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    steps = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<TestCase %r>' % self.username


# 定义task表结构
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    testcase_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.username

#定义task服务
class TaskService(Resource):
    def get(self):
        # 根据测试任务id获取用例id,若找不到对应的测试用例，则返回全部
        id = request.args.get("id")
        if id:
            task = Task.query.filter_by(id=id).first()
            return {
                "msg":"ok",
                "body":task.testcase_id
            }
        else:
            tasks = Task.query.all()
            return {
                "msg":"ok",
                "body":[task.testcase_id for task in tasks]
            }

    def post(self):
        # 添加任务
        task = Task(
            # 将post请求报文中的json相关信息存入数据库
            name = request.json.get("name"),
            testcase_id = request.json.get("testcase_id")
        )

        db.session.add(task)
        db.session.commit()
        return {
            "msg":"ok"
        }

    def put(self):
        # 找出要执行的任务
        id = request.json.get('id')
        if id:
            task = Task.query.filter_by(id=id).first()
            testcases_info=[]
            for id in json.loads(task.testcases):
                testcase = TestCase.query.filter_by(id=int(id)).first()
                case_info = {
                    'name': testcase.name,
                    'steps': testcase.steps
                }
                testcases_info.append(case_info)

            task_info = {
                'id': task.id,
                'testcases': testcases_info
            }
            # os.system('pytest xx') use jenkins replace
            jenkins: Jenkins = app.config['jenkins']
            jenkins['test_platform_testcases'].invoke(
                build_params={
                    'task': json.dumps(task_info)
                }
            )
            return {
                'msg': 'ok'
            }

# 定义服testcase务
class TestCaseService(Resource):
    def get(self):
        # 获取资源
        testcases = TestCase.query.all()
        res = [{
            "id": testcase.id,
            "name": testcase.name,
            "description": testcase.description,
            # "steps": json.loads(testcase.steps)
            "steps":testcase.steps
        } for testcase in testcases
        ]
        return {
            "body": res
        }
    def post(self):
        # 上传编辑用例
        # 往数据库存数据
        testcase = TestCase(
            name = request.json.get("name"),
            description = request.json.get("description"),
            steps = request.json.get("steps")
            # steps = json.dumps(request.json.get('steps'))
        )
        # 往db追加数据
        db.session.add(testcase)
        # 提交
        db.session.commit()

        return {
            "msg":"ok"
        }

    def put(self):
        pass

# 往api添加服务，及其路由
api.add_resource(TestCaseService, "/testcase")
api.add_resource(TaskService, "/task")

if __name__ == "__main__":
    app.run(debug=True, port=8384)

