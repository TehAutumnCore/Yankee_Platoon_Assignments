"""
from django.core.exceptions import ValidationError
import re

def validate_name_format(name):
    error_message = 'Name must be in the format "First M. Last"'
    
    # Regex to match the format "First M. Last" or "First Last"
    regex = r'^[A-Z][a-z]+(?: [A-Z]\. )?[A-Z][a-z]+$'

    valid_name = re.match(regex, name)

    if valid_name:
        return name
    else:
        raise ValidationError(error_message, params={'name': name})
    

def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    
    # Regex to check if the email ends with @school.com
    regex = r'^[a-zA-Z0-9._%+-]+@school\.com$'  # Matches any valid email that ends with @school.com
    
    valid_email = re.match(regex, email)
    
    if valid_email:
        return email
    else:
        raise ValidationError(error_message, params={'email': email})
    

def validate_combination_format(combination):
    error_message = 'Combination must be in the format "12-12-12"'
    
    # Regex for "12-12-12" format (three pairs of digits separated by dashes)
    regex = r'^\d{2}-\d{2}-\d{2}$'  # Matches the format of "12-12-12"
    
    valid_combination = re.match(regex, combination)
    
    if valid_combination:
        return combination
    else:
        raise ValidationError(error_message, params={'combination': combination})
"""    



from django.core.exceptions import ValidationError
import re

def validate_name_format(value):
    """
    Validator for the "First M. Last" name format.
    """
    name_pattern = re.compile(r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$')
    if not name_pattern.match(value):
        raise ValidationError('Name must be in the format "First Middle Initial. Last"')

def validate_school_email(value):
    """
    Validator for the school email format ending with "@school.com".
    """
    email_pattern = re.compile(r'^.+@school\.com$')
    if not email_pattern.match(value):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')

def validate_combination_format(value):
    """
    Validator for the format "12-12-12" (ensures there are numbers only).
    """
    combination_pattern = re.compile(r'^\d{2}-\d{2}-\d{2}$')
    if not combination_pattern.match(value):
        raise ValidationError('Combination must be in the format "12-12-12"')