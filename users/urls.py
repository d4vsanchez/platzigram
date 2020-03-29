"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView

# Views
from users import views

urlpatterns = [
    # Posts
    path(
        "<str:username>",
        TemplateView.as_view(template_name="users/detail.html"),
        name="detail",
    ),
    # Management
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("me/profile", views.update_profile_view, name="update_profile"),
]
