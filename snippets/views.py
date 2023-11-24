from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from .models import Snippet
from django.urls import reverse


# Create your views here.
class CreateSnippet(CreateView):
    model = Snippet
    fields = ["language", "body"]
    template_name = "snippets/create-snippet.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("snippet-detail", args=[self.object.id])


class SnippetDetail(DetailView):
    model = Snippet
    template_name = "snippets/snippet-detail.html"
    context_object_name = "snippet"
