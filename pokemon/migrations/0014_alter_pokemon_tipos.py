# Generated by Django 4.0.4 on 2022-06-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0013_alter_pokemon_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='tipos',
            field=models.ManyToManyField(blank=True, null=True, to='pokemon.tipo'),
        ),
    ]