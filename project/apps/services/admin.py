from django.contrib import admin

from .models import Category, Service


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'category']
    list_filter = ['category']

    search_fields = ['title', 'description']
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('published',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()



admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)