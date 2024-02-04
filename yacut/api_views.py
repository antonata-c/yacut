from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import validate_post_data, get_unique_short_id


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_url(short):
    urlmap = URLMap.query.filter_by(short=short).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден',
                              HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    validate_post_data(data)
    urlmap = URLMap()
    # какой из способов лучше? и есть ли более удачная идея?
    # data['custom_id'] = f'http://localhost/{data['custom_id']}' костыль №1
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify({
        'url': urlmap.original,
        'short_link': f'http://localhost/{data["custom_id"]}'  # костыль №2
    }), HTTPStatus.CREATED
