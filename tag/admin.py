from django.contrib import admin

from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'event')


# Register your models here.
admin.site.register(Tag)