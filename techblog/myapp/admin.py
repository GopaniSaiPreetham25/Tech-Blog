# from django.contrib import admin
# from django.apps import apps

# # Lazy model import to avoid circular import
# techblog = apps.get_model('myapp', 'techblog')

# @admin.register(techblog)
# class TechblogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'discription', 'photo')  # Display these fields in admin
#     search_fields = ('title', 'discription')          # Add search functionality
#     list_filter = ('title',)                          # Filter options by title


from django.contrib import admin
from .models import techblog

class TechblogAdmin(admin.ModelAdmin):
    list_display = ('title', 'discription', 'photo')

admin.site.register(techblog, TechblogAdmin)
