# Generated by Django 4.0.4 on 2022-05-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_projetos_nome_do_projeto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_cadeira', models.CharField(max_length=100)),
                ('ano', models.IntegerField(default=0)),
                ('semestre', models.IntegerField(default=1)),
                ('ects', models.IntegerField(default=0)),
                ('avaliacao', models.CharField(max_length=100)),
                ('total_ects', models.CharField(max_length=100)),
            ],
        ),
    ]
