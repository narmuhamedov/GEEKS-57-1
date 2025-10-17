from django.urls import path
from . import views

urlpatterns = [
    path('student_list/', views.ReadStudent.as_view(), name='student_list'),
    path('student_list/<int:id>/update/', views.UpdateStudent.as_view(), name='update_student'),
     path('student_list/<int:id>/delete/', views.DeleteStudent.as_view(), name='delete_student'),


    path('create_student/', views.CreateStudent.as_view(), name='create_student'),
]