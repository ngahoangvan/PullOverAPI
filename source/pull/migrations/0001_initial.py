# Generated by Django 2.0.5 on 2018-11-13 10:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'pull_category',
            },
        ),
        migrations.CreateModel(
            name='GenericPull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.TextField()),
                ('details', models.TextField()),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='pull.Categories')),
            ],
            options={
                'db_table': 'pull_generic',
            },
        ),
        migrations.CreateModel(
            name='SpecificPull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=50)),
                ('generic_pull', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generic_pull', to='pull.GenericPull')),
            ],
            options={
                'db_table': 'pull_specific',
            },
        ),
    ]