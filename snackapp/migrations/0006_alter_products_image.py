# Generated by Django 3.2.9 on 2021-11-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snackapp', '0005_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(blank=True, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4QOjaXf9Kp3OBcQOQoOqF17obRPZ759bXsSSZIboGEcT6NvAmLSuYeqxYSUDoGQtb_4U&usqp=CAU', max_length=500, null=True),
        ),
    ]
