from flask import Flask, request
from flask_restful import Resource, Api

from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from .model import Model, Student

app = Flask(__name__)
api = Api(app)

model = Model()

class Predict(Resource):
    
    def __init__(self):
        self.student = Student(**request.args)

    def get(self):
        result = model.predict(self.student)
        return jsonify(result)

api.add_resource(Predict, '/predict/')

if __name__ == '__main__':
    app.run(port='5002')
