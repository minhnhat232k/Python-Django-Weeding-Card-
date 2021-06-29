from django.contrib import admin

# Register your models here.
from .models import Subscribe4
# Register your models here.
class PostEmployee(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Subscribe4, PostEmployee)