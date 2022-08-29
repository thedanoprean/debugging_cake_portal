from django.contrib import admin
from cake_user.models.user_model import User, Role
from cake_user.models.user_profile_model import UserProfile

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserProfile)