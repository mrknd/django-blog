from django.contrib import admin
from assignments.models import About, SocialLink


class AboutAdmin(admin.ModelAdmin):     # Remove add button from admin-panel if we have 1 title
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)