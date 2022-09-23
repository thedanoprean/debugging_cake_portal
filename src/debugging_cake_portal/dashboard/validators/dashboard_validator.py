from decimal import *

from django.core.exceptions import ValidationError


def validate_roles(type_roles):
    if not isinstance(type_roles, str) or not type_roles.isalpha():
        raise ValidationError("'role' must be a string")


def validate_nr_users(nr_users):
    if isinstance(nr_users, Decimal) and isinstance(nr_users, float) and not isinstance(nr_users, int):
        raise ValidationError("'nr_users' must be a integer value")


def validate_nr_comments(nr_comments):
    if isinstance(nr_comments, Decimal) and isinstance(nr_comments, float) and not isinstance(nr_comments, int):
        raise ValidationError("'nr_comments' must be a integer value")


def validate_nr_posts(nr_posts):
    if isinstance(nr_posts, Decimal) and isinstance(nr_posts, float) and not isinstance(nr_posts, int):
        raise ValidationError("'nr_posts' must be a integer value")


def validate_nr_roles(nr_roles):
    if isinstance(nr_roles, Decimal) and isinstance(nr_roles, float) and not isinstance(nr_roles, int):
        raise ValidationError("'nr_roles' must be a integer value")