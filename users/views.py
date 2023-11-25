from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import customUserCreationForm
from .models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    form_class = customUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class BaseTemplateView(DetailView):
    model = CustomUser
    context_object_name = "user"
    template_name = "snippets/base.html"

    def get_queryset(self):
        return CustomUser.objects.get(pk=self.request.user.pk)
