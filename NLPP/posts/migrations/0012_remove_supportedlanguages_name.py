# Generated by Django 3.0 on 2020-01-23 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_supportedlanguages_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supportedlanguages',
            name='name',
        ),
    ]