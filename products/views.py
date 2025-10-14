from django.shortcuts import render
from . import models



def seach_view(request):
    query = request.GET.get('s', '')
    products_lst = models.Product.objects.filter(title__icontains=query) if query else models.Product.none
    context = {
        'products': products_lst,
        's': query
    }
    return render(request, template_name='products/all_products.html', context=context)

#1.Фронтендщик создает в html шаблоне форму и внутри есть name=s
#2.Прописываете логику поиска
#3.Делаете акцент на all_products
#4.Действие на context из логики all_products
#5.Создание ссылки на поиск
#6.Передача ссылки на html шаблон в тег form




def all_products(request):
    if request.method == 'GET':
        products = models.Product.objects.all().order_by('-id')
        return render(request, 'products/all_products.html', 
                      {'products': products})



def chinese_food(request):
    if request.method == 'GET':
        products = models.Product.objects.filter(tags__name='#Китайская кухня').order_by('-id')
        return render(request, 'products/chinese_food.html', 
                      {'products': products})

def drinks(request):
    if request.method == 'GET':
        products = models.Product.objects.filter(tags__name='#Напитки').order_by('-id')
        return render(request, 'products/drinks.html', 
                      {'products': products})
    

#1.Создаете модель
#2.Проводим миграции
#3.Регистрация модели в admin.py
#4.Прописание логики во views.py
#5.Передача данных на html страницу
#6.Создание ссылок на вашу логику во views.py в файле urls.py
#7.Подключение startapp в главных urls.py