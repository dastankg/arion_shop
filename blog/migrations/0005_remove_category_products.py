# Generated by Django 4.2.2 on 2023-06-11 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_photo_alter_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
    ]
