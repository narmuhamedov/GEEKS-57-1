from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('chinese_food/', views.chinese_food, name='chinese_food'),
    path('drinks/', views.drinks, name='drinks'),
    path('search/', views.seach_view, name='search'),
]