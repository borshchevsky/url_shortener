from random import choices
import string


def generate_short_url():

    """Функция генерирует короткий url"""

    chars = string.digits + string.ascii_letters
    return ''.join(choices(chars, k=5))
