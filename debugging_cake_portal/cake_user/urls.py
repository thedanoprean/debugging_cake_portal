from django.contrib.auth.views import LogoutView
from django.urls import path
from .views.homepage_view import homepage
from .views.login_view import LoginView
from .views.register_view import register


app_name = "cake_user"

urlpatterns = [
    path('', homepage),
    path('login/', LoginView.as_view(template_name='cake_user/login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]