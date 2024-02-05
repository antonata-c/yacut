import string

LETTERS_DIGITS = string.ascii_letters + string.digits

REDIRECT_URL = 'redirect_view'

MIN_ORIGINAL_SIZE = 1
MAX_ORIGINAL_SIZE = 256
MIN_SHORT_SIZE = 0
MAX_GENERATED_SHORT = 6
MAX_USER_SHORT = 16
MAX_GENERATE_REPETITIONS = 1000

SHORT_ID_REGEX = rf'^[a-zA-Z0-9]{{{MIN_SHORT_SIZE},{MAX_USER_SHORT}}}$'

NOT_UNIQUE_SHORT_ID = 'Предложенный вариант короткой ссылки уже существует.'
