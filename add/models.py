from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Education(models.Model):
    # user =models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=100, null=False, blank=False)
    field_of_study = models.CharField(max_length=100, null=False, blank=False)
    start_date =models.DateField()
    end_date =models.DateField()
    grade = models.IntegerField(null=False, blank=False)
    activities_and_societies = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    status = models.CharField( max_length=100)
    my_file = models.FileField(null=True, blank=True, upload_to='documents/' )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.school_name
    
