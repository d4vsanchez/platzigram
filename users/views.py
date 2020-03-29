"""User views"""

# Django
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Models
from users.models import Profile

# Forms
from users.forms import ProfileForm


@login_required
def update_profile_view(request):
    """Update a user's profile view."""

    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data["website"]
            profile.phone_number = data["phone_number"]
            profile.biography = data["biography"]
            profile.picture = data["picture"]
            profile.save()

            return redirect("update_profile")
    else:
        form = ProfileForm()

    return render(
        request,
        "users/update_profile.html",
        {"profile": profile, "user": request.user, "form": form},
    )


def login_view(request):
    """Login view."""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("feed")
        else:
            return render(
                request, "users/login.html", {"error": "Wrong username or password"}
            )
    return render(request, "users/login.html")


def signup_view(request):
    """Signup view."""
    if request.method == "POST":
        username = request.POST["username"]
        passwd = request.POST["passwd"]
        passwd_confirmation = request.POST["passwd_confirmation"]

        if passwd != passwd_confirmation:
            return render(
                request,
                "users/signup.html",
                {"error": "Password confirmation does not match"},
            )

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except:
            return render(
                request, "users/signup.html", {"error": "Username already taken"}
            )
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]

        profile = Profile.objects.create(user=user)
        return redirect("login")
    return render(request, "users/signup.html")


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect("login")
