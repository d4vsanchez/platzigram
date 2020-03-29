"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path("", views.PostsFeedView.as_view(), name="feed"),
    path("posts/new/", views.create_post, name="create"),
]