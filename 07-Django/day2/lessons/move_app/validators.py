from django.core.exceptions import ValidationError
import re

def validate_move_name(move_name):
    error_message = "invalid Move Name format"
    
    regex = r'^[a-zA-Z]+ ?[a-zA-Z]+$'
    
    valid_name = re.match(regex, move_name)
    
    if valid_name:
        return move_name
    else:
        raise ValidationError(error_message, params={'move_name': move_name})
    