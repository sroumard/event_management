# Generated by Django 5.1.1 on 2024-11-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
