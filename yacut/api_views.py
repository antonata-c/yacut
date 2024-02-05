from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app
from .constants import REDIRECT_URL
from .error_handlers import InvalidAPIRequest
from .models import URLMap

ID_NOT_FOUND = 'Указанный id не найден'
EMPTY_REQUEST_BODY = 'Отсутствует тело запроса'
FIELD_IS_REQUIRED = '"{field}" является обязательным полем!'


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_url(short):
    url_map = URLMap.get_by_short(short)
    if url_map is None:
        raise InvalidAPIRequest(ID_NOT_FOUND,
                                HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIRequest(EMPTY_REQUEST_BODY)
    required_fields = ('url',)
    for field in required_fields:
        if field not in data:
            raise InvalidAPIRequest(FIELD_IS_REQUIRED.format(field=field))
    url_map = URLMap.create(data)
    return jsonify({
        'url': url_map.original,
        'short_link': url_for(
            REDIRECT_URL,
            short=url_map.short,
            _external=True
        )
    }), HTTPStatus.CREATED
