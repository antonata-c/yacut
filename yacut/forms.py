from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (DataRequired, Length, Optional, Regexp,
                                ValidationError)

from .constants import MAX_ORIGINAL_SIZE, MAX_USER_SHORT, SHORT_ID_REGEX
from .models import NOT_UNIQUE_SHORT, URLMap

ORIGINAL_LINK = 'Добавьте оригинальную длинную ссылку'
REQUIRED_FIELD = 'Обязательное поле'
ADD_ID = 'Добавьте идентификатор'
CREATE_TEXT = 'Создать'


class URLMapForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LINK,
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            Length(max=MAX_ORIGINAL_SIZE)
        ]
    )
    custom_id = StringField(
        ADD_ID,
        validators=[
            Length(max=MAX_USER_SHORT),
            Regexp(SHORT_ID_REGEX),
            Optional()
        ]
    )
    submit = SubmitField(CREATE_TEXT)

    def validate_custom_id(self, field):
        if field.data and URLMap.get(field.data) is not None:
            raise ValidationError(NOT_UNIQUE_SHORT)
