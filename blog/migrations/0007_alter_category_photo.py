# Generated by Django 4.2.2 on 2023-06-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, default='media/default.jpg', upload_to='category_images/'),
        ),
    ]
