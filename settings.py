import os
from string import ascii_letters, digits

SHORT_SIZE = 16  # хорошая ли идея хранить константы здесь?
LETTERS_DIGITS = ascii_letters + digits


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
