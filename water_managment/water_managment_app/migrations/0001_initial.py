# Generated by Django 5.1.3 on 2024-11-18 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Areas', models.CharField(blank=True, max_length=30, null=True)),
                ('Description', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ConnectionNo', models.IntegerField(blank=True, null=True)),
                ('Report', models.FileField(blank=True, null=True, upload_to='')),
                ('Date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('Type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notification', models.CharField(blank=True, max_length=30, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterQualityTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QualityStatus', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact', models.BigIntegerField(blank=True, null=True)),
                ('PaymentStatus', models.CharField(blank=True, max_length=30, null=True)),
                ('DueDate', models.DateField(blank=True, null=True)),
                ('CONNECTION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='water_managment_app.connectiontable')),
            ],
        ),
        migrations.CreateModel(
            name='ReaderTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, max_length=10, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='water_managment_app.logintable')),
            ],
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, max_length=10, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='water_managment_app.logintable')),
            ],
        ),
        migrations.AddField(
            model_name='connectiontable',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='water_managment_app.usertable'),
        ),
        migrations.CreateModel(
            name='ComplaintTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Reply', models.CharField(blank=True, max_length=100, null=True)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='water_managment_app.usertable')),
            ],
        ),
    ]
