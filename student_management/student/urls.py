from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'), 
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/update/<int:student_id>/', views.update_student, name='update_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
]