from datetime import datetime

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        # мне показалось, что этот словарь касается лишь этой ф-ции,
        # или есть место хранения поудачнее?
        key_to_field = {
            'url': 'original',
            'custom_id': 'short'
        }
        for key, field in key_to_field.items():
            if key in data:
                setattr(self, field, data[key])
