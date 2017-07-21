# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Bairro')),
                ('address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('price', models.IntegerField(verbose_name='Cachê')),
                ('contact', models.CharField(max_length=100, verbose_name='Contato')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'ordering': ['state', 'city', 'neighborhood', 'name'],
                'verbose_name_plural': 'Artistas',
                'verbose_name': 'Artista',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Cidade')),
            ],
            options={
                'ordering': ['state', 'name'],
                'verbose_name_plural': 'Cidades',
                'verbose_name': 'Cidade',
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('owner', models.CharField(max_length=100, verbose_name='Responsável')),
                ('opened', models.CharField(max_length=100, verbose_name='Horário de funcionamento')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Bairro')),
                ('address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('contact', models.CharField(max_length=100, verbose_name='Contato')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.City', verbose_name='Cidade')),
            ],
            options={
                'ordering': ['state', 'city', 'name'],
                'verbose_name_plural': 'Espaços',
                'verbose_name': 'Espaço',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Estado')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Estados',
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gener', models.CharField(max_length=100, verbose_name='Gênero')),
            ],
            options={
                'ordering': ['gener'],
                'verbose_name_plural': 'Gêneros',
                'verbose_name': 'Gênero',
            },
        ),
        migrations.AddField(
            model_name='club',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='artist',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.City', verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='artist',
            name='gener',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Style', verbose_name='Gênero'),
        ),
        migrations.AddField(
            model_name='artist',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State', verbose_name='Estado'),
        ),
    ]