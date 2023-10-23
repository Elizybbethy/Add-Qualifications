from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationModelAdmin(admin.ModelAdmin):
    list_display =[
        'school_name', 'degree', 'field_of_study', 'start_date', 'end_date', 'grade', 'activities_and_societies', 'description', 'status', 'my_file'
    ]
