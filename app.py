from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
#from flask_pymongo import PyMongo
from thisisatest import a
import pymongo
import re
from collections import OrderedDict
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'about' : 'Hello World!'}

#     def post(self):
#         some_json = request.get_json()
#         return {'you sent' : some_json}, 201


class Get_Id(Resource):
    def get(self):
        app_name_dict = a()
        return render_template("base.html", app_name_dict = app_name_dict)

    # def post(self):
        # take input of which application name is needed


# class Control_type_table():
#     def get(self):




api.add_resource(Get_Id, '/')
# api.add_resource(Control_type_table, '/ctt')
# api.add_resource(Get_control_type, '/gct')
# api.add_resource(control_name_table, '/cnt')

if __name__ == '__main__' :
    app.run(debug = True)