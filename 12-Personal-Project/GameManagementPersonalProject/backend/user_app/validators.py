from django.core.exceptions import ValidationError
import re

# def validate_username(username):
#     error_messages = 'Improper username Format.'
#     regex = "^[A-Za-z][A-Za-z0-9_]{7,29}$" #8-30 chars inclusive, only alpha chars and underscores containing a-zA-Z and 0-9, first char must be a alpha char
    
#     good_name = re.match(regex, username)
    
#     if good_name:
#         return username
#     raise ValidationError(error_message, params={'username': username
# })

#-----------------------------------------------------------------------
def validate_email(email):
    error_messages = 'Improper email Format.'
    regex = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    #checks if string is a valid email by checking the "personal info" the @ symbol and the domain ex: personal_info@domain.com
    
    good_email = re.match(regex, email)
    
    if good_email:
        return email
    raise ValidationError(error_message, params={'email': email})

#-----------------------------------------------------------------------
# def validate_password(password):
#     error_messages = 'Improper password Format.'
#     regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$" 
#     #8 min chars, 1 upper letter, 1 lower letter, 1 digit, one special character
    
#     good_password = re.match(regex, password)
    
#     if good_password:
#         return password
#     raise ValidationError(error_message, params={'password': password})