from django.views import generic
from django.urls import reverse_lazy
from ..forms.register_form import RegisterForm


class RegisterView(generic.CreateView):

    form_class = RegisterForm
    template_name = 'cake_user/register.html'
    success_url = reverse_lazy('cake_user:login')
