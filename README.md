# Training-AIHomework
There are 2 dockerized services pingService and reaciverService, pingService creats a POST request to an endpoint which accepts a body containing a url key and corresponding link, I.E. {'url': 'https://www.foobar.com'} and the reciverServie simply return an hardcoded HTTP response

## Requirements 

We are using flask as the web framework 

```bash
pip install Flask==1.1.2 flask-restplus==0.13.0 requests==2.25.1 Werkzeug==0.16.1
```

```yml
version: "3.7"

services:
    ping:
        build: ./pingService
        container_name: ping-service
        restart: always
        expose:
          - 8080
    
    recive:
        build: ./reciverService
        container_name: reciver-service
        restart: always
```


```Dockerfile
FROM python:3

WORKDIR /usr/src/app

COPY APP_NAME .

RUN pip install Flask==1.1.2 flask-restplus==0.13.0 requests==2.25.1 Werkzeug==0.16.1

CMD ["python", "./APP_NAME"]
```

## Usage

pingService

```python

from flask import Flask, Response
from flask_restplus import Resource, Api, fields
import requests

app = Flask(__name__)
api = Api(app)

#Creating an endpoint to store the post request if needed in future
endpoint = api.model("URL", {"url": fields.String("The URL.")})

@api.route('/api/v1/ping') #creating route
class PingService(Resource):
    @api.expect(endpoint)
    def post(self):
        r = requests.get(api.payload['url']) #getting the payload from the url
        return r.json(), 201

@api.route('/health')
class Health(Resource):
    def get(self):
        return '', 200
             
if __name__ == '__main__':
    app.run()
```

reciverService

```python

from flask import Flask, Response
from flask_restplus import Resource, Api, fields
import requests

app = Flask(__name__)
api = Api(app)
       
@api.route('/api/v1/info')
class ReciverService(Resource):
    def get(self):
        return {'Receiver': 'Cisco is the best!'}	#returns hardcoded string as an HTTP response

if __name__ == '__main__':
    app.run()
    

```
## Contributing
Pull requests are welcome.

Please make sure to update tests as appropriate.
