from django.core.exceptions import ValidationError
import re

def validate_subject_name(name):
    regex= r"^[A-Z][a-z]+$"
    good_name = re.match(regex, name)
    if good_name:
        return good_name
    raise ValidationError("Improper Subject Format")

def validate_professor_name(name):
    regex = r"^Professor [A-Z][a-z]+$"
    good_name = re.match(regex, name)
    if good_name:
        return good_name
    raise ValidationError("Improper Professor name")