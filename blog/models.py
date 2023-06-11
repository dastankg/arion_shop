from django.db import models
from django.db.models import Model
from django.db.models.deletion import DO_NOTHING, SET_NULL


class Category(models.Model):
    category_name = models.CharField("Название", max_length=200)
    is_active = models.BooleanField("Активный", default=True)
    photo = models.ImageField("Фотография", upload_to='category_images/', blank=True, default='default.jpg')
    date_added = models.DateTimeField("Дата добавления", auto_now_add=True)
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




def product_image_upload_to(instance, filename):
    category_id = instance.product.category.category_name
    product_name = instance.product.name
    return f'product_images/{category_id}/{product_name}/{filename}'




class Product(models.Model):
    name = models.CharField("Имя", max_length=200)
    price = models.IntegerField("Цена", blank=False)
    description = models.TextField("Описание", blank=True)
    category = models.ForeignKey(Category, on_delete=DO_NOTHING, blank=False, null=False, verbose_name="Категория")
    date_added = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def return_photo(self):
        return Photo.objects.filter(product_id=self.pk)

    @property
    def return_characteristics(self):
        return Characteristic.objects.filter(product_id=self.pk)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Photo(models.Model):
    image = models.ImageField("Фотография", upload_to=product_image_upload_to, default="default.jpg")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Фотографии", default="")

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

class Characteristic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')
    name = models.CharField("Параметр", max_length=100)
    value = models.CharField("Значение", max_length=100)

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
