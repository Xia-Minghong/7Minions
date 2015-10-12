from django.contrib import admin

from .models import Feedback





class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('event', 'content', 'rating')
    list_filter = ('event__name',)
    ordering = ['event__name']


    def get_queryset(self, request):
        if request.user.is_superuser:
            return Feedback.objects.all()
        return Feedback.objects.filter(event__organizer__id = 1)

# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)


