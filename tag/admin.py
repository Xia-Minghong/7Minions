from django.contrib import admin

from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','tag', 'event')
    list_filter = ('tag',)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Tag.objects.all()
        return Tag.objects.filter(event__organizer__id = 1)


# Register your models here.
admin.site.register(Tag, TagAdmin)