# Generated by Django 3.2.9 on 2021-11-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snackapp', '0006_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4QOjaXf9Kp3OBcQOQoOqF17obRPZ759bXsSSZIboGEcT6NvAmLSuYeqxYSUDoGQtb_4U&usqp=CAU', max_length=500),
        ),
    ]
