"""Posts views"""

# Utilities
from datetime import datetime

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Forms
from posts.forms import PostForm


@login_required
def list_posts(request):
    """List existing posts"""
    posts = [
        {
            "title": "Mont Blanc",
            "user": {
                "name": "Yesica Cortes",
                "picture": "https://picsum.photos/60/60/?image=1027",
            },
            "timestamp": datetime.now(),
            "photo": "https://i.picsum.photos/id/658/600/600.jpg",
        },
        {
            "title": "Via Lactea",
            "user": {
                "name": "C. Vander",
                "picture": "https://picsum.photos/60/60/?image=1005",
            },
            "timestamp": datetime.now(),
            "photo": "https://i.picsum.photos/id/656/600/600.jpg",
        },
        {
            "title": "Nuevo auditorio",
            "user": {
                "name": "Thespianartist",
                "picture": "https://picsum.photos/60/60/?image=883",
            },
            "timestamp": datetime.now(),
            "photo": "https://i.picsum.photos/id/657/600/600.jpg",
        },
    ]
    return render(request, "posts/feed.html", {"posts": posts})


@login_required
def create_post(request):
    """Create new post view."""
    profile = request.user.profile

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("feed")
    else:
        form = PostForm()

    return render(
        request,
        template_name="posts/new.html",
        context={"form": form, "user": request.user, "profile": profile},
    )
