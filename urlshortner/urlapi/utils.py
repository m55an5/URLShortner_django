from random import choice
from string import ascii_letters

MAX_CODE_LENGTH=6
CHARS=ascii_letters

def generate_random_code(chars=CHARS):
    return "".join(
        [choice(chars) for _ in range(MAX_CODE_LENGTH)])


def generate_short_url(url_model_class):
    code=generate_random_code()

    if url_model_class.objects.filter(short_url=code).exists():
        return generate_short_url(url_model_class)

    return code