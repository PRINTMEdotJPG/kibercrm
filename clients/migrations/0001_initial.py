# Generated by Django 5.1.3 on 2024-12-11 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('phone_number', models.CharField(max_length=16, verbose_name='Номер телефона')),
                ('passport_serial', models.CharField(blank=True, max_length=4, null=True, verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(blank=True, max_length=7, null=True, verbose_name='Номер паспорта')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Адрес регистрации')),
                ('subscription_price', models.IntegerField(verbose_name='Стоимость абонемента')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('child_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='clients.parent')),
            ],
            options={
                'verbose_name': 'Ребенок',
                'verbose_name_plural': 'Дети',
            },
        ),
    ]