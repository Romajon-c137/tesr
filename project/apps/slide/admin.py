from django.contrib import admin

from .models import Slide


class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', 'is_active', 'author']
    list_filter = ['author', 'is_active']
    list_editable = ('is_active',)

    search_fields = ['title', 'description']
    readonly_fields = [ 'updated_at', 'created_at', 'author']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Slide, SlideAdmin)
