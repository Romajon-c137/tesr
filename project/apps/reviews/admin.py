from django.contrib import admin
from .models import Review
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'published')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
    list_editable = ('published',)


admin.site.register(Review, ReviewAdmin)