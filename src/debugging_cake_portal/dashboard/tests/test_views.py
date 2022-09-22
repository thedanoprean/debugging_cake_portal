# Project settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debugging_cake_portal.debugging_cake_portal.settings")
import django

django.setup()

from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.http import Http404
import pytest
from datetime import date

from dashboard.views import index, pivot_data, pivot_update, dashboard_with_pivot
from dashboard.models import Analysis


class TestDashboardViews:

    def test_ok_get_all(self):
        """
        Test that checks if get returns all Dashboard objects from db
        """
        factory = APIRequestFactory()
        request = factory.get(path="/dashboard/")
        view = index(request)

        # get
        response = view(request)

        assert response.status_code == status.HTTP_200_OK
        assert (len(response.context_data['hospitalization_list']) == len(Analysis.objects.all()))

    def test_get_ok_detail_1(self):
        """
        test with a valid id
        """
        factory = APIRequestFactory()
        request = factory.get("/hospitalization/<int:pk>/")
        view = HospitalizationDetailView.as_view()

        hospitalization = Hospitalization(
            symptoms="{'head':'intense pain'}",
            hospitalization_date=date.today(),
        )

        hospitalization.save()

        # get
        response = view(request, pk=hospitalization.pk)

        assert response.status_code == status.HTTP_200_OK
        assert response.context_data['hospitalization_report'].pk == hospitalization.pk

    def test_get_ko_detail_1(self):
        """
        test with an invalid id
        """
        factory = APIRequestFactory()
        request = factory.get("/hospitalization/<int:pk>/")
        view = HospitalizationDetailView.as_view()

        Hospitalization.objects.filter(pk=999).delete()

        # get
        with pytest.raises(Http404):
            response = view(request, pk=999)