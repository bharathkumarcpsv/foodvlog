from django.contrib import admin
from .models import *
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(catag,catadmin)
class proadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','price','stock','img','available']
    list_editable = ['price','stock','img','available']
admin.site.register(products,proadmin)

# Register your models here.
