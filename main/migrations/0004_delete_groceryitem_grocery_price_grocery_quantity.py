# Generated by Django 4.0.6 on 2022-07-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_grocery_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GroceryItem',
        ),
        migrations.AddField(
            model_name='grocery',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grocery',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
