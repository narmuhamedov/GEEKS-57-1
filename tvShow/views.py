from django.shortcuts import render, get_object_or_404
#Модуль httpResponse - отвечает за вывод одиночного сообщения
from django.http import HttpResponse
from . import models
from django.views import generic


#ListView
def film_list_view(request):
    if request.method == 'GET':
        films = models.Films.objects.all()
        context = {
            'films': films,
        }
        return render(request, template_name='films/films_list.html', context=context)


#DetailView

class FilmDetailView(generic.DetailView):
    template_name = 'films/film_detail.html'
    context_object_name = 'film_id'

    def get_object(self, *args, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Films, id=film_id)


# def film_detail_view(request, id):
#     if request.method == 'GET':
#         film_id = get_object_or_404(models.Films, id=id)
#         context = {
#             'film_id': film_id,
#         }
#         return render(request, template_name='films/film_detail.html', context=context)





def first_message_view(request):
    if request.method == 'GET':
        return HttpResponse('Привет GEEKS 57-1🤓')
    

def second_message_view(request):
    if request.method == 'GET':
        return HttpResponse('😀😃😄😁')
