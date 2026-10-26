
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'university_id',
        'age',
        'date_of_birth',
        'salary',
    )
    search_fields = ('full_name', 'university_id')
    list_filter = ('age', 'date_of_birth')
