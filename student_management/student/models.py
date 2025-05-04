from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=100, unique=True)
    student_admission_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name
    
    def get_student_details(self):
        return {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "student_class": self.student_class,
            "student_email": self.student_email,
            "student_admission_date": self.student_admission_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
