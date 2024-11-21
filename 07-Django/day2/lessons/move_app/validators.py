from django.core.exceptions import ValidationError
import re

def validate_move_name(move_name):
    error_message = 'Improper Move Name Format.'
    regex = r"^[a-zA-Z]+ ?[a-zA-Z]+$"

    good_name = re.match(regex, move_name)

    if good_name:
        return move_name
    raise ValidationError(error_message, params={'move_name': move_name})