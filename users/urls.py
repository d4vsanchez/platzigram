"""Users URLs."""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # Posts
    path("<str:username>", views.UserDetailView.as_view(), name="detail",),
    # Management
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("me/profile", views.update_profile_view, name="update_profile"),
]
