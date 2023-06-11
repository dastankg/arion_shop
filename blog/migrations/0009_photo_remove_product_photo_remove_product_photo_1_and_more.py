# Generated by Django 4.2.2 on 2023-06-11 11:59

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_category_photo_alter_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=blog.models.product_image_upload_to)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_3',
        ),
        migrations.AddField(
            model_name='product',
            name='photos',
            field=models.ManyToManyField(blank=True, to='blog.photo'),
        ),
    ]
