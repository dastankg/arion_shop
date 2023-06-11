from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Characteristic, Category, Photo
from .forms import CharacteristicForm
from django.contrib.auth.models import User, Group


# Удаление раздела "Пользователи"
admin.site.unregister(User)
admin.site.unregister(Group)


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1
    form = CharacteristicForm

class PhotoInline(admin.TabularInline):
    model = Photo



# Определение класса администратора для модели Product
class ProductAdmin(admin.ModelAdmin):
    # Определение полей, которые будут отображаться в списке продуктов
    list_display = ['name', 'price', 'category']
    inlines = [PhotoInline, CharacteristicInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
