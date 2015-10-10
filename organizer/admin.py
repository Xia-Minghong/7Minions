from django.contrib import admin

from .models import Organizer

class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


# Register your models here.
admin.site.register(Organizer, OrganizerAdmin)