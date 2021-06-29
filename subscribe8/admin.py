from django.contrib import admin

# Register your models here.
from .models import Subscribe8
# Register your models here.
class PostEmployee(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Subscribe8, PostEmployee)