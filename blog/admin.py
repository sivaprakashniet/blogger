# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import ClueType, Clue
# Register your models here.
class ClueTypeAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(ClueType,ClueTypeAdmin)

class ClueAdmin(admin.ModelAdmin):
    list_display=('title',)
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Clue,ClueAdmin)