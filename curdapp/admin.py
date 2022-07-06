from django.contrib import admin
from .models import Students

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll','name','address','email','record','date']

admin.site.register(Students,StudentAdmin)

