from django.urls import path
from .views import (
    CreateSnippet,
    SnippetDetail,
    EditSnippet,
    DeleteSnippet,
    UserSnippetsList,
)

urlpatterns = [
    path("", CreateSnippet.as_view(), name="create-snippet"),
    path("snippet/<slug:pk>/", SnippetDetail.as_view(), name="snippet-detail"),
    path("edit-snippet/<slug:pk>/", EditSnippet.as_view(), name="edit-snippet"),
    path("delete-snippet/<slug:pk>/", DeleteSnippet.as_view(), name="delete-snippet"),
    path("profile/", UserSnippetsList.as_view(), name="profile"),
]
