from django.contrib import admin
from .models import *

class techblogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo']

admin.site.register(techblog, techblogAdmin)


