from django.core.exceptions import ValidationError


def validate_title(title):
    if not isinstance(title, str) or not title.isalpha():
        raise ValidationError("'title' must be a string")
