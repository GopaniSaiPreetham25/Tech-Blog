
from django.contrib import admin
from .models import techblog

class TechblogAdmin(admin.ModelAdmin):
    list_display = ('title', 'discription', 'photo')

admin.site.register(techblog, TechblogAdmin)
