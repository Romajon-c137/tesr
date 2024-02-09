from django.contrib import admin

from .models import Category, News


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'edited_at', 'published', 'category', 'author']
    list_filter = ['author', 'category']

    search_fields = ['title', 'description']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = [ 'edited_at', 'created_at', 'author']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()



admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)