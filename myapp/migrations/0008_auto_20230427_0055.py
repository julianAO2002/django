# Generated by Django 2.2.28 on 2023-04-27 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alumno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='cuit',
            new_name='dni',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='monotributista',
        ),
    ]
