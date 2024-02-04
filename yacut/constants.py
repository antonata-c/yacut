import string

LETTERS_DIGITS = string.ascii_letters + string.digits

SHORT_SIZE = 16
SHORT_ID_REGEX = r'^[a-zA-Z0-9]*$'

INCORRECT_SHORT_ID = 'Указано недопустимое имя для короткой ссылки'
NOT_UNIQUE_SHORT_ID = 'Предложенный вариант короткой ссылки уже существует.'
FIELD_REQUIRED = '"{field}" является обязательным полем!'
ID_NOT_FOUND = 'Указанный id не найден'
EMPTY_REQUEST_BODY = 'Отсутствует тело запроса'
