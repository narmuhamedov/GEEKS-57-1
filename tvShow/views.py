from django.shortcuts import render
#Модуль httpResponse - отвечает за вывод одиночного сообщения
from django.http import HttpResponse



def first_message_view(request):
    if request.method == 'GET':
        return HttpResponse('Привет GEEKS 57-1🤓')
    

def second_message_view(request):
    if request.method == 'GET':
        return HttpResponse('😀😃😄😁')
