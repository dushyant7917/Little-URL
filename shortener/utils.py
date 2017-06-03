import string
import random
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size = SHORTCODE_MIN, chars = string.ascii_lowercase + string.ascii_uppercase + string.digits):
    '''
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code
    '''
    # The above code is written in just one line below
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size = SHORTCODE_MIN):
    new_code = code_generator(size = size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode = new_code).exists()
    if qs_exists:
        return create_shortcode(size = size)
    return new_code
