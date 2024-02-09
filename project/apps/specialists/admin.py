from django.contrib import admin

from .models import Department, Person, Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'slug')
    list_filter = ('published',)
    search_fields = ('name', 'experience')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('published',)


class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'published', 'department', 'role']
    list_filter = ['department', 'roles', 'role', 'published']

    search_fields = ['name', 'description']
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ('published',)
    

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()



admin.site.register(Department, DepartmentAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Role, RoleAdmin)