# Generated by Django 2.0.6 on 2018-06-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('texto', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
                ('URLimagen', models.CharField(blank=True, max_length=80, null=True)),
                ('fechapublicacion', models.DateTimeField()),
                ('categorias', models.CharField(choices=[(('0',), 'Deportes'), (('1',), 'Ocio'), (('2',), 'Tecnologia'), (('3',), 'Salud'), (('4',), 'Naturaleza')], max_length=1)),
            ],
        ),
    ]
