import random
import string

def random_char(char_num: int) -> str:
    """
    Random char generator to use with email.

    :param char_num: character number as integer to generate random letters.
    :return: Random string with given char_num length.
    """
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def generate_mail() -> str:
    """
    Generates and returns random email for headers.

    :return: Returns generated random email as string.
    """
    return random_char(random.randint(5,8))+"@"+random_char(random.randint(3,6))+".com"

def headers() -> dict:
    """
    Generates headers to use in request.

    :return: headers as dict.
    """
    headers = { 
        'User-Agent': 'My User Agent 1.0', 
        'From': generate_mail()
    }
    return headers
