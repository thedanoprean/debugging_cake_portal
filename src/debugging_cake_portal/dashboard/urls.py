from django.urls import path
from .views import pivot_data, dashboard_with_pivot

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data/', pivot_data, name='pivot_data'),
]
