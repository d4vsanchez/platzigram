from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from users import views as users_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Posts
    path("", include(("posts.urls", "posts"), namespace="posts")),
    # User
    path("users/", include(("users.urls", "users"), namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
