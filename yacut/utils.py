import random
import re

from .constants import (FIELD_REQUIRED, INCORRECT_SHORT_ID, LETTERS_DIGITS,
                        NOT_UNIQUE_SHORT_ID, SHORT_ID_REGEX, SHORT_SIZE)
from .error_handlers import InvalidAPIRequest
from .models import URLMap


def get_unique_short_id(size=6):
    while True:
        short = ''.join(random.choices(LETTERS_DIGITS, k=size))
        if not URLMap.query.filter_by(short=short).first():
            break
    return short


# Стоит ли для этой функции добавить файл validators?
def validate_post_data(data):
    required_fields = ('url',)
    for field in required_fields:
        if field not in data:
            raise InvalidAPIRequest(FIELD_REQUIRED.format(field=field))
    short = data.get('custom_id')
    if len(short) > SHORT_SIZE:
        raise InvalidAPIRequest(INCORRECT_SHORT_ID)
    if re.match(SHORT_ID_REGEX, short) is None:
        raise InvalidAPIRequest(INCORRECT_SHORT_ID)
    if URLMap.query.filter_by(short=short).first():
        raise InvalidAPIRequest(
            NOT_UNIQUE_SHORT_ID
        )
