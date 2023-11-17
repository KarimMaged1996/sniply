from django.urls import path
from .views import CreateSnippet

urlpatterns = [
    path("", CreateSnippet.as_view(), name="create-snippet"),
]
