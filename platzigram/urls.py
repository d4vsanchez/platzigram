from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", posts_views.list_posts, name="feed"),
    path("users/login", users_views.login_view, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
