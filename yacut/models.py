import random
import re
from datetime import datetime

from . import db
from .constants import (LETTERS_DIGITS, MAX_GENERATE_REPETITIONS,
                        MAX_GENERATED_SHORT, MAX_ORIGINAL_SIZE, MAX_USER_SHORT,
                        NOT_UNIQUE_SHORT_ID, SHORT_ID_REGEX)
from .exceptions import InvalidAPIRequest

INCORRECT_SHORT_ID = 'Указано недопустимое имя для короткой ссылки'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text(MAX_ORIGINAL_SIZE), nullable=False)
    short = db.Column(db.String(MAX_USER_SHORT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @classmethod
    def create(cls, data):
        print(data)
        if 'custom_id' not in data or not data.get('custom_id'):
            data['custom_id'] = cls.get_unique_short_id()
        cls.validate_post_data(data)
        original_field = 'url' if 'url' in data else 'original_link'
        url_map = URLMap(
            original=data.get(original_field),
            short=data.get('custom_id')
        )
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @classmethod
    def get_by_short(cls, short):
        return cls.query.filter_by(short=short).first()

    @classmethod
    def get_unique_short_id(cls, size=MAX_GENERATED_SHORT):
        short = None
        for i in range(MAX_GENERATE_REPETITIONS):
            short = ''.join(random.choices(LETTERS_DIGITS, k=size))
            if not cls.get_by_short(short):
                break
        return short

    @staticmethod
    def validate_post_data(data):
        short = data.get('custom_id')
        if len(short) > MAX_USER_SHORT:
            raise InvalidAPIRequest(INCORRECT_SHORT_ID)
        if re.match(SHORT_ID_REGEX, short) is None:
            raise InvalidAPIRequest(INCORRECT_SHORT_ID)
        if URLMap.get_by_short(short):
            raise InvalidAPIRequest(
                NOT_UNIQUE_SHORT_ID
            )
