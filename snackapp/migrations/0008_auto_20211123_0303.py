# Generated by Django 3.2.9 on 2021-11-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snackapp', '0007_alter_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='money',
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
