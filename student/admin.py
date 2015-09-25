from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Matric Number',   {'fields': ['matric_no']}),
        ('Name',            {'fields': ['name'], 'classes': ['collapse']}),
    ]

admin.site.register(Student, StudentAdmin)