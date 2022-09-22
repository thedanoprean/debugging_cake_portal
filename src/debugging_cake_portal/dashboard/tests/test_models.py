# Project settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debugging_cake_portal.settings")
import django

django.setup()

from django.core.exceptions import ValidationError
import pytest
from decimal import *

from dashboard.models import Analysis


@pytest.mark.db
class TestAnalysis:

    @pytest.mark.parametrize(
        "nr_users, nr_comments, nr_posts, nr_roles",
        [
            pytest.param(10, 10, 10, 10, id="Test number of users"),
            pytest.param(10, 10, 10, 10, id="Test number of comments"),
            pytest.param(10, 10, 10, 10, id="Test number of posts"),
            pytest.param(10, 10, 10, 10, id="Test number of roles"),
        ]
    )
    def test_successful_validation(self, nr_users, nr_comments, nr_posts, nr_roles):
        """
        Test that validates Analysis objects with correct parameters and values
        """
        analysis = Analysis(
            nr_users=nr_users,
            nr_comments=nr_comments,
            nr_posts=nr_posts,
            nr_roles=nr_roles
        )

        try:
            analysis.full_clean()
        except:
            assert False
        else:
            assert True

    @pytest.mark.parametrize(
        "nr_users, nr_comments, nr_posts, nr_roles",
        [
            pytest.param(9999999999, 10, 10, 10, id="Test maximum number of users"),
            pytest.param(10, 9999999999, 10, 10, id="Test maximum number of comments"),
            pytest.param(10, 10, 999999999, 10, id="Test maximum number of posts"),
            pytest.param(10, 10, 10, 9999999999, id="Test maximum number of roles"),
        ]
    )
    def test_unsuccessful_validation(self, nr_users, nr_comments, nr_posts, nr_roles):
        """
        Test that attempts to validate an Analysis object with parameters of correct types, but values out of range
        """
        analysis = Analysis(
            nr_users=nr_users,
            nr_comments=nr_comments,
            nr_posts=nr_posts,
            nr_roles=nr_roles
        )

        with pytest.raises(ValidationError):
            analysis.full_clean()

    @pytest.mark.parametrize(
        "nr_users, nr_comments, nr_posts, nr_roles",
        [
            pytest.param(Decimal('10.12'), 10, 10, 10, id="Test number of users with float"),
            pytest.param(10, [10, 12], 10, 10, id="Test number of comments with list"),
            pytest.param(10, 10, "nr_posts", 10, id="Test number of posts with string"),
            pytest.param(10, 10, 10, {"10": 10}, id="Test number of roles with dict"),
        ]
    )
    def test_type_error_validation(self, nr_users, nr_comments, nr_posts, nr_roles):
        """
        Test that attempts to validate Analysis objects with parameters of the wrong type
        """
        analysis = Analysis(
            nr_users=nr_users,
            nr_comments=nr_comments,
            nr_posts=nr_posts,
            nr_roles=nr_roles
        )

        with pytest.raises(ValidationError):
            analysis.full_clean()
