from django.urls import path
from .views import CreateSnippet, SnippetDetail

urlpatterns = [
    path("", CreateSnippet.as_view(), name="create-snippet"),
    path("snippet/<slug:pk>/", SnippetDetail.as_view(), name="snippet-detail"),
]
