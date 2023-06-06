# Generated by Django 2.2.28 on 2023-04-27 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20230425_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('cuit', models.CharField(max_length=11)),
                ('monotributista', models.BooleanField()),
                ('cursos', models.ManyToManyField(related_name='alumnos', to='myapp.Curso')),
            ],
            options={
                'verbose_name_plural': 'Alumnos',
            },
        ),
    ]
