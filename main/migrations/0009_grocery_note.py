# Generated by Django 4.0.6 on 2022-07-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_grocery_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='note',
            field=models.CharField(default='nothing', max_length=500),
            preserve_default=False,
        ),
    ]