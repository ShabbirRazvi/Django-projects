from django.contrib import admin
from .models import Student
# Register your models here.


class Studentadmin(admin.ModelAdmin):
    list_display = ['id', 'sn', 'sr', 'sb', 'sc']
    search_fields = ['sn', 'sr']
    admin.site.site_title = "PR SOFTWARES"
    admin.site.site_header = "Students"
    admin.site.index = "Student Details"


admin.site.register(Student, Student_admin)
