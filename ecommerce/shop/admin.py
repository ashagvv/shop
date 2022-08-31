from django.contrib import admin

# Register your models here.
from .models import Category,Product




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class Productadmin(admin.ModelAdmin):
    list_display = ['name', 'slug','price','available','stock','created','updated']
    prepopulated_fields = {'slug': ('name',)}
    list_editable =['price','stock','available']
    list_per_page = 20
admin.site.register(Product, Productadmin)



