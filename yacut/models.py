import random
import re
from datetime import datetime

from . import db
from .constants import (LETTERS_DIGITS, MAX_GENERATE_REPETITIONS,
                        MAX_GENERATED_SHORT, MAX_ORIGINAL_SIZE, MAX_USER_SHORT,
                        SHORT_ID_REGEX)

INCORRECT_ORIGINAL = 'Указано недопустимое имя для оригинальной ссылки'
INCORRECT_SHORT = 'Указано недопустимое имя для короткой ссылки'
NOT_UNIQUE_SHORT = 'Предложенный вариант короткой ссылки уже существует.'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text(MAX_ORIGINAL_SIZE), nullable=False)
    short = db.Column(db.String(MAX_USER_SHORT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def create(original, short, from_api=True):
        if not short:
            short = URLMap.get_unique_short()
        if from_api:
            if len(short) > MAX_USER_SHORT:
                raise ValueError(INCORRECT_SHORT)
            if len(original) > MAX_ORIGINAL_SIZE:
                raise ValueError(INCORRECT_ORIGINAL)
            if re.match(SHORT_ID_REGEX, short) is None:
                raise ValueError(INCORRECT_SHORT)
            if URLMap.get(short) is not None:
                raise ValueError(NOT_UNIQUE_SHORT)
        url_map = URLMap(
            original=original,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @staticmethod
    def get(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def get_unique_short(size=MAX_GENERATED_SHORT,
                         charset=LETTERS_DIGITS,
                         repetitions=MAX_GENERATE_REPETITIONS):
        short = ''
        for _ in range(repetitions):
            short = ''.join(random.choices(charset, k=size))
            if not URLMap.get(short):
                break
        return short
