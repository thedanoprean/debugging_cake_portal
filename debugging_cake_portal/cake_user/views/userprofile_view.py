from django.shortcuts import render
from ..models.user_model import User


def profile(request, pk):
    userprofile = User.objects.get(id=pk)
    context = {
        'userprofile': userprofile
    }
    return render(request, 'cake_user/user_profile.html', context)
