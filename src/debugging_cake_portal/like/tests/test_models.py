# Project settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debugging_cake_portal.settings")
import django

django.setup()
from django.core.exceptions import ValidationError
import pytest
from decimal import *
from like.models import Like


@pytest.mark.db
class TestLike:
    @pytest.mark.parametrize(
        "user, post, value",
        [
            pytest.param(1, 1, True, id="Test user"),
            pytest.param(10, 10, True, id="Test post"),
            pytest.param(10, 10, True, id="Test value"),
        ]
    )
    def test_successful_validation_OK(self, user, post, value):
        """
        Test that validates Like objects with correct parameters and values
        """
        like = Like(
            user=user,
            post=post,
            value=value,
        )
        try:
            like.full_clean()
        except:
            assert False
        else:
            assert True

    @pytest.mark.parametrize(
        "user, post, value",
        [
            pytest.param(1, 1, 1, id="Test value with int"),
            pytest.param(10, 10, 1, id="Test value with int"),
            pytest.param(10, 10, 1, id="Test value with int"),
        ]
    )
    def test_unsuccessful_validation_KO(self, user, post, value):
        """
        Test that attempts to validate an Like object with parameters of correct types, but values out of range
        """
        like = Like(
            user=user,
            post=post,
            value=value,
        )
        with pytest.raises(ValidationError):
            like.full_clean()

    @pytest.mark.parametrize(
        "user, post, value",
        [
            pytest.param(Decimal('10.12'), 10, 10, 10, id="Test user with float"),
            pytest.param(10, [10, 12], 10, 10, id="Test post with list"),
            pytest.param(10, 10, "nr_posts", 10, id="Test value with string"),
        ]
    )
    def test_type_error_validation_KO(self, user, post, value):
        """
        Test that attempts to validate Like objects with parameters of the wrong type
        """
        like = Like(
            user=user,
            post=post,
            value=value,
        )
        with pytest.raises(ValidationError):
            like.full_clean()
