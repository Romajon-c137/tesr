from django.contrib import admin
from .models import Page, FreeCall, Lab, Result


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'status', 'edited_at', 'is_show']
    list_filter = ['status', 'menu', 'is_show']
    list_editable = ('is_show',)
    search_fields = ['title', 'name']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['created_at', 'edited_at', 'order']


class FreeCallAdmin(admin.ModelAdmin):
    list_filter = ['full_name', 'subject', 'status']
    list_display = ['full_name', 'phone_number', 'e_mail', 'status']
    readonly_fields = ['message', 'full_name', 'e_mail', 'phone_number', 'subject', 'town']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
    
    def has_add_permission(self, request):
        return False


class LabAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'oder_number', 'pin', 'status']
    list_filter = ['status', 'gender', 'order_date']
    search_fields = ['full_name']
    def has_add_permission(self, request):
        return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False


class ResultAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     return False

admin.site.register(Page, PageAdmin)
admin.site.register(FreeCall, FreeCallAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Lab, LabAdmin)