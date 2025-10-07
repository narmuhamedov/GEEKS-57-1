from django.urls import path
from . import views

urlpatterns = [
    path('student_list/', views.readStudent, name='student_list'),
    path('student_list/<int:id>/update/', views.updateStudent, name='update_student'),
     path('student_list/<int:id>/delete/', views.deleteStudent, name='delete_student'),


    path('create_student/', views.createStudent, name='create_student'),
]