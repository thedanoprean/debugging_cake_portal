# Project settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debugging_cake_portal.settings")
import django

django.setup()

from rest_framework.test import APIRequestFactory
from rest_framework import status
import pytest

from dashboard.views import dashboard_with_pivot
from dashboard.models import Analysis


class TestDashboardViews:

    def test_ok_get_all(self):
        """
        Test that checks if dashboard_with_pivot returns all Dashboard objects from db
        """
        factory = APIRequestFactory()
        request = factory.get(path="dashboard/")
        view = dashboard_with_pivot(request)
        response = view
        # nr_users = Users.all() ; make request ; check users; delete user/add_commend/add_reply; make_request; check again
        assert response.status_code == status.HTTP_200_OK
        print(response.content)
        #assert (len(response.data) == len(Analysis.objects.all()))
