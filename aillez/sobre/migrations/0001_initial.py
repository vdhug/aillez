# Generated by Django 2.0 on 2020-11-14 20:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Escreva sobre os compromissos da empresa', max_length=80, verbose_name='Título')),
                ('texto', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Compromissos da empresa',
            },
        ),
        migrations.CreateModel(
            name='SobreNos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Escreva sobre a empresa', max_length=80, verbose_name='Título')),
                ('texto', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Sobre a empresa',
            },
        ),
    ]
