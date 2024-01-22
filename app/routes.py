from flask import Blueprint, request
from app.controller import get_index, post_question

routes_blueprint = Blueprint('routes_blueprint', __name__)

@routes_blueprint.route('/', methods=['GET'])
def index():
    return get_index()

@routes_blueprint.route('/question', methods=['POST'])
def question():
    data = request.json  
    return post_question(data)

def create_routes(app):
    app.register_blueprint(routes_blueprint)