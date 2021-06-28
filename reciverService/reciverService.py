from flask import Flask, Response
from flask_restplus import Resource, Api, fields
import requests

app = Flask(__name__)
api = Api(app)
       
@api.route('/api/v1/info')
class ReciverService(Resource):
    def get(self):
        return {'Receiver': 'Cisco is the best!'}

if __name__ == '__main__':
    app.run()
    