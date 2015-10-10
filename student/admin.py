from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class FriendshipInline(admin.TabularInline):        #(admin.StackedInline):
    model = Friendship
    fk_name = 'from_student'

class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('from_student', 'to_student')

class RegistrationInline(admin.TabularInline):        #(admin.StackedInline):
    model = Registration
    fk_name = 'student'

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'event')


class BookmarkInline(admin.TabularInline):        #(admin.StackedInline):
    model = Bookmark
    fk_name = 'student'

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'event')

# class UserInline(admin.StackedInline):
#     model = User
#     fk_name = 'student'
#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'matric_no')
#     fieldsets = [
#         ('Matric Number',   {'fields': ['matric_no']}),
#         ('Name',            {'fields': ['name'], 'classes': ['collapse']}),
#     ]
#     search_fields = ['name', 'matric_no']
#     inlines = [UserInline, FriendshipInline]

class StudentInline(admin.StackedInline):
    model=Student
    fk_name = 'user'

class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'student')
    inlines = [StudentInline]




#admin.site.register(Student, StudentAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Bookmark, BookmarkAdmin)