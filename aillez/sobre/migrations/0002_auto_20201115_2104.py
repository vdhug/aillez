# Generated by Django 2.0 on 2020-11-15 21:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Escreva sobre a empresa', max_length=80, verbose_name='Título')),
                ('sobre_nos', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Escreva sobre a empresa')),
                ('compromissos', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Escreva sobre os compromissos da empresa')),
            ],
            options={
                'verbose_name_plural': 'Sobre a empresa',
            },
        ),
        migrations.DeleteModel(
            name='Compromisso',
        ),
        migrations.DeleteModel(
            name='SobreNos',
        ),
    ]
