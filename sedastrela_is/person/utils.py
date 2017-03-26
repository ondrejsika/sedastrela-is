import random
import string


RANDOM_CHARACTERS = string.ascii_lowercase + string.digits


def get_random_string(length, choices=RANDOM_CHARACTERS):
    return ''.join(random.choice(choices) for _ in range(length))