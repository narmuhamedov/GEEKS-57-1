from django.db import models


class Films(models.Model):
    image = models.ImageField(upload_to='films/', verbose_name='загрузите картинку фильма')
    title = models.CharField(max_length=100, verbose_name='напишите название фильма')
    description = models.TextField(verbose_name='укажите описание к фильму')
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Фантастика', 'Фантастика'),
        ('Боевики', 'Боевики')
    )
    #default - атрибут по умолчанию
    genre = models.CharField(max_length=100, choices=GENRE, default='Фантастика')
    #blank = True поле не обязательно для заполнения
    director = models.CharField(max_length=100, blank=True, verbose_name='укажите режисера')
    quantity = models.PositiveIntegerField(default=1, verbose_name='укажите кол-во серий')
    trailer = models.URLField(verbose_name='укажите ссылку с youtube')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    #Доп задание домашнее  - посмотреть документацию django-models

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
        

    

