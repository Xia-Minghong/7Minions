from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Event.objects.all()
        return Event.objects.filter(organizer = 1)


# Register your models here.
admin.site.register(Event, EventAdmin)
