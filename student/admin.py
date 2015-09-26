from django.contrib import admin
from .models import Student, Friendship

# Register your models here.

class FriendshipInline(admin.TabularInline):        #(admin.StackedInline):
    model = Friendship
    fk_name = 'from_student'

class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('from_student', 'to_student')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'matric_no')
    fieldsets = [
        ('Matric Number',   {'fields': ['matric_no']}),
        ('Name',            {'fields': ['name'], 'classes': ['collapse']}),
    ]
    search_fields = ['name', 'matric_no']
    inlines = [FriendshipInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Friendship, FriendshipAdmin)