"""Users URLs."""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # Management
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("me/profile/", views.UpdateProfileView.as_view(), name="update_profile"),
    # Posts
    path("<str:username>", views.UserDetailView.as_view(), name="detail",),
]
