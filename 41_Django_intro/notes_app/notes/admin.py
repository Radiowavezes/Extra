from django.contrib import admin
from .models import Notes
from .models import Category

class NotesAdmin(admin.ModelAdmin):
    list_display = ('text', 'title', 'reminder', 'pub_date')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('headline', 'all_notes')

admin.site.register(Notes, NotesAdmin)
admin.site.register(Category)
