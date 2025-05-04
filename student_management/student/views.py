from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def student_list(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'students': students})

def student_detail(request, student_id):
    return render(request, 'student_detail.html', {'student': Student.objects.get(student_id=student_id)})

def create_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_class = request.POST.get('student_class')
        student_email = request.POST.get('student_email')
        student_admission_date = request.POST.get('student_admission_date')
        # Check if student with this email already exists
        if Student.objects.filter(student_email=student_email).exists():
            messages.error(request, f"Student with email {student_email} already exists!")
            return render(request, 'create_student.html', {'error_message': 'Email already exists'})
        student = Student(
            student_name=student_name,
            student_class=student_class,
            student_email=student_email,
            student_admission_date=student_admission_date
        )
        student.save()
        return render(request, 'index.html', {'students': Student.objects.all().order_by('-created_at')})
    return render(request, 'create_student.html')

def update_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.student_name = request.POST.get('student_name')
        student.student_class = request.POST.get('student_class')
        student.student_email = request.POST.get('student_email')
        student.student_admission_date = request.POST.get('student_admission_date')
        # Check if student with this email already exists
        if Student.objects.exclude(student_id=student_id).filter(student_email=student.student_email).exists():
            messages.error(request, f"Student with email {student.student_email} already exists!")
            return render(request, 'update_student.html', {'student': student, 'error_message': 'Email already exists'})
        student.status = "updated"
        student.save()
        messages.success(request, f"Student {student.student_name} updated successfully!")
        return redirect('student_list')
    return render(request, 'update_student.html', {'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.status = "deleted"
        student.save()
        messages.success(request, f"Student {student.student_name} deleted successfully!")
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})

