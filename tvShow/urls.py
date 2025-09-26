from django.urls import path
from . import views


urlpatterns = [
    path('first_message/', views.first_message_view, name='first_message'),
    path('second_message/', views.second_message_view, name='second_message'),
]

