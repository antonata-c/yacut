from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app, db
from .constants import EMPTY_REQUEST_BODY, ID_NOT_FOUND
from .error_handlers import InvalidAPIRequest
from .models import URLMap
from .utils import get_unique_short_id, validate_post_data


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_url(short):
    urlmap = URLMap.query.filter_by(short=short).first()
    if urlmap is None:
        raise InvalidAPIRequest(ID_NOT_FOUND,
                                HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIRequest(EMPTY_REQUEST_BODY)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    validate_post_data(data)
    urlmap = URLMap(
        original=data.get('url'),
        short=data.get('custom_id')
    )
    db.session.add(urlmap)
    db.session.commit()
    return jsonify({
        'url': urlmap.original,
        'short_link': url_for(
            'redirect_view',
            short=urlmap.short,
            _external=True
        )
    }), HTTPStatus.CREATED
