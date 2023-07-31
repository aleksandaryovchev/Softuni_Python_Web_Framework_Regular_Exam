from django.contrib import admin
from .models import Profile, Post, Comment

# Register your models here
admin.site.register(Post)
admin.site.register(Comment)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'favorite_player')
    list_filter = ('country', 'favorite_player')
    search_fields = ('user__username', 'user__email', 'country', 'favorite_player')

    # Customize the admin interface as needed
    fieldsets = (
        ('Personal Information', {
            'fields': ('user', 'bio', 'profile_picture', 'birth_date')
        }),
        ('Favorites', {
            'fields': ('country', 'favorite_player', 'favorite_match')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        # Make certain fields read-only for non-superuser admins
        if not request.user.is_superuser:
            return 'user', 'bio', 'profile_picture', 'birth_date', 'country', 'favorite_player', 'favorite_match'
        return super().get_readonly_fields(request, obj)

    def has_add_permission(self, request):
        # Disable adding new profiles from the admin interface
        return False
