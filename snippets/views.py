from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
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


class EditSnippet(UpdateView):
    model = Snippet
    fields = ["body"]
    template_name = "snippets/edit-snippet.html"

    def get_success_url(self):
        return reverse("snippet-detail", args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add extra context here
        context[
            "language"
        ] = self.object.language  # Assuming 'language' is a field in your model
        context["slug"] = self.object.id
        return context


class DeleteSnippet(DeleteView):
    model = Snippet
    success_url = "/"
    success_message = "Your Snippet Was Deleted Successfully"
    template_name = "snippets/delete-snippet.html"
    context_object_name = "snippet"
