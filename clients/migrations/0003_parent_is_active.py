# Generated by Django 5.1.3 on 2025-02-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_parent_linked_location_child_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]
