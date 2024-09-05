from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    make = models.CharField(max_length=256, verbose_name='Марка автомобиля')
    model = models.CharField(max_length=256, verbose_name='Модель автомобиля')
    year = models.CharField(max_length=10, verbose_name='Год выпуска')
    description = models.CharField(max_length=1024, verbose_name='Описание автомобиля')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и Время создания записи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и Время последнего обновления записи')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f'{self.make} {self.model}'


class Comment(models.Model):
    content = models.CharField(max_length=1024, verbose_name='Содержание комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и Время создания комментария')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль', related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.car.make} {self.car.model} | {self.content}'
