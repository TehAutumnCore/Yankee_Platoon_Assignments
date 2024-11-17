from django.core.exceptions import Validators
import re

def validate_subject_name(name):
    regex = r"^[A-Z][a-z]