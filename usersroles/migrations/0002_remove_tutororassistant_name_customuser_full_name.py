# Generated by Django 5.1.3 on 2024-11-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersroles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutororassistant',
            name='name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='ФИО'),
        ),
    ]
