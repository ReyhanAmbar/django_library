from django.contrib import admin
# Register your models here.
from .models import Library, RequestedBook, Contact, Student


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('reason','title')


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'category', 'availability')


@admin.register(RequestedBook)
class RequestedBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_surname', 'student_no', 'student_contact', 'student_email')
