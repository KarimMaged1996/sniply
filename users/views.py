from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import customUserCreationForm


# Create your views here.
class RegisterView(CreateView):
    form_class = customUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
