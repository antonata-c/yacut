from random import choices

from .error_handlers import InvalidAPIUsage
from settings import SHORT_SIZE, LETTERS_DIGITS

from .models import URLMap


def get_unique_short_id(size=6):
    short = ''.join(choices(LETTERS_DIGITS, k=size))
    while URLMap.query.filter_by(short=short).first():
        short = ''.join(choices(LETTERS_DIGITS, k=size))
    return short


# Стоит ли для этой функции добавить файл validators?
# Хорошее ли решение вынести ее из вьюшки?
def validate_post_data(data):
    # required_fields = ('url',)
    # error_fields = list(
    #     filter(lambda field: field not in data, required_fields)
    # )
    if 'url' not in data:
        raise InvalidAPIUsage(f'"url" является обязательным полем!')
    short = data.get('custom_id')
    if len(short) > SHORT_SIZE:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=short).first():
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.'
        )