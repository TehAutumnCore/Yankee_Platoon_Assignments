from django.core.exceptions import ValidationError
import re

def validate_pokemon_name(name):
    error_message = "Improper name format."
    
    regex = r'^[A-Z][a-z]*$'
    
    good_name = re.match(regex,name)
    
    if good_name:
        return name
    else:
        raise ValidationError(error_message,params={'name':name})
    
    # valid_pokemon_name_has_no_spaces
    #     "name has spaces"
    # valid_pokemon_name_has_no_numbers
    #     "name has numbers"