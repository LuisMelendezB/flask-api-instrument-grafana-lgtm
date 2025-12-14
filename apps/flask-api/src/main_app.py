from flask import Flask, jsonify
from flask_restx import Api
from endpoints.endpoints import endpoints_list

app = Flask(__name__)
debug = True

api = Api(app)

def register_endpoint(api, resource, url):
    api.add_resource(resource, url)

for endpoint in endpoints_list:
    register_endpoint(api, endpoint['resource'], endpoint['url'])

if __name__ == '__main__':
    app.run(debug=debug)