from django.views.generic import ListView, DetailView
from tag.models.tag_model import Tag


class TagListView(ListView):
    model = Tag
    context_object_name = 'tag_list'
    template_name = "tag_list_template.html"


class TagDetailView(DetailView):
    model = Tag
    context_object_name = 'tag_report'
    template_name = "tag_detail_template.html"

