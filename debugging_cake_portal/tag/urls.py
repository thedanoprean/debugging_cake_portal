from tag.views.tag_views import TagListView, TagDetailView
from tag.views.rest import TagRestView
from django.urls import path

app_name = "tag"

urlpatterns = [
    path('', TagListView.as_view()),
    path('<int:pk>/', TagDetailView.as_view()),

    # Django Rest Views
    path('rest/', TagRestView.as_view()),
    path('rest/<int:pk>/', TagRestView.as_view()),
]
