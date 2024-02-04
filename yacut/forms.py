from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from settings import SHORT_SIZE


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Добавьте оригинальную длинную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Добавьте идентификатор',
        validators=[Length(max=SHORT_SIZE), Optional()]
    )
    submit = SubmitField('Создать')
