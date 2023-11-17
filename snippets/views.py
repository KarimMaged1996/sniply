from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import Snippet


# Create your views here.
class CreateSnippet(CreateView):
    model = Snippet
    fields = ["language", "body"]
    template_name = "snippets/create-snippet.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
