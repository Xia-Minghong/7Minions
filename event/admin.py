from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('name', 'location', 'description')
    readonly_fields = ('participant_list_field',)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Event.objects.all()
        return Event.objects.filter(organizer = 1)

    # def participant_list_field(self):
    #     return self.participant_list_field()

# Register your models here.
admin.site.register(Event, EventAdmin)
