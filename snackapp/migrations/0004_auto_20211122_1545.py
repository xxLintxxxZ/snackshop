# Generated by Django 3.2.9 on 2021-11-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snackapp', '0003_rename_name_products_prodname'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='money',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]