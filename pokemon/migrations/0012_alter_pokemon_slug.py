# Generated by Django 4.0.4 on 2022-06-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0011_pokemon_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', max_length=100),
        ),
    ]