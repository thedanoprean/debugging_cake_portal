from django.template import loader
from django.http import HttpResponse

from notifications.models import Notification


# Create your views here.

def show_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)
    template = loader.get_template('notifications.html')
    context = {
        'notifications': notifications,
    }

    return HttpResponse(template.render(context, request))


# def count_notifications(request):
#     count_notifications = 0
#     if request.user.is_authenticated:
#         count_notifications = Notification.objects.all().count()
#         print(count_notifications)
#     context = {
#         'count_notifications': count_notifications
#     }
#     template = loader.get_template('navbar.html')
#     # return HttpResponse(template.render(context, request))
#     return {'count_notifications': count_notifications}