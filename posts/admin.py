# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ("pk", "title", "photo", "user")
    list_display_links = ("pk", "title")
    search_fields = ("user__email", "user__username", "title")
    list_filter = ("created", "modified", "user__is_active")

    fieldsets = (
        ("Photo information", {"fields": (("title", "photo")),}),
        ("Author information", {"fields": (("user",)),}),
    )
