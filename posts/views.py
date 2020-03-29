"""Posts views"""

# Utilities
from datetime import datetime

# Django
from django.shortcuts import render


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
