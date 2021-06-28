from flask import Flask, Response
from flask_restplus import Resource, Api, fields
import requests

app = Flask(__name__)
api = Api(app)

endpoint = api.model("URL", {"url": fields.String("The URL.")})

@api.route('/api/v1/ping')
class PingService(Resource):
    @api.expect(endpoint)
    def post(self):
        r = requests.get(api.payload['url'])
        return r.json(), 201

@api.route('/health')
class Health(Resource):
    def get(self):
        return '', 200
             
if __name__ == '__main__':
    app.run()
    
    
