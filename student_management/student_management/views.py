from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def student_list(request):
    return HttpResponse("<h1>List of Students</h1>")

def student_detail(request, student_id):
    return HttpResponse(f"<h1>Details of Student {student_id}</h1>")