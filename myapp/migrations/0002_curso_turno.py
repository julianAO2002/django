# Generated by Django 2.2.28 on 2023-04-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Mañana'), (2, 'Tarde'), (3, 'Noche')], null=True),
        ),
    ]
