from django.contrib.auth import get_user_model
from django.db import models

CHOICES = [('for car', 'для машины'), ('for home', 'для дома'), ('for garden', 'для сада')]


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название продукта')
    category = models.CharField(max_length=30, choices=CHOICES, default=CHOICES[0][0],
                                verbose_name='Категории')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images', null=True, blank=True, default='default.png', verbose_name='Картинка')

    def __str__(self):
        return f"{self.id}. {self.product_name} : {self.category}"

    class Meta:
        db_table = 'Product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='reviews', on_delete=models.CASCADE,
                               verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='product', on_delete=models.CASCADE,
                                verbose_name='Продукт')
    text_review = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    rating = models.IntegerField(default=0, verbose_name='Оценка')
    active_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.id}. {self.author} : {self.product}, {self.rating}, {self.created_at}"

    class Meta:
        db_table = 'Review'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
