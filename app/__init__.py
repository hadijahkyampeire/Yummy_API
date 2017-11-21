from flask import Flask, request, jsonify
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# from api.instance import models

# local import
from .instance.config import app_config
# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from app.api.models import Category
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    db.init_app(app)


@app.route('/categories/', methods=['POST', 'GET'])
def categories():
    if request.method == "POST":
        name = str(request.data.get('name', ''))
        if name:
            category = Category(name=name)
            category.save()
            response = jsonify({
                'id': category.id,
                'name': category.name,
                'date_created': category.date_created,
                'date_modified': category.date_modified
            })
            response.status_code = 201
            return response
        else:
            # GET
            categories = Category.get_all()
            results = []

            for category in categories:
                obj = {
                    'id': category.id,
                    'name': category.name,
                    'date_created': category.date_created,
                    'date_modified': category.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    return app
