from flask import Flask
from flask_restx import Api

from endpoints.endpoints import endpoints_list


def register_endpoints(api: Api) -> None:
    """Register all API resources/endpoints."""
    for endpoint in endpoints_list:
        api.add_resource(endpoint["resource"], endpoint["url"])


def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(
        app,
        title="Flask API"
        )
    register_endpoints(api)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)