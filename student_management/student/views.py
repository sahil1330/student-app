from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    return render(request, 'index.html')

def student_list(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'students': students})

def student_detail(request, student_id):
    return render(request, 'student_detail.html', {'student': Student.objects.get(student_id=student_id)})