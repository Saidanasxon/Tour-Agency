# Generated by Django 5.0.6 on 2024-06-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_travel_category_alter_travel_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
