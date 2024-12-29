# Generated by Django 5.1.3 on 2024-11-19 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_managment_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubadminTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, max_length=10, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Actions', models.CharField(blank=True, max_length=100, null=True)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='water_managment_app.logintable')),
            ],
        ),
    ]
