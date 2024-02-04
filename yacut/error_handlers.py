from flask import jsonify, render_template

from . import app
from .exceptions import InvalidAPIRequest


@app.errorhandler(InvalidAPIRequest)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
