# Generated by Django 3.0 on 2020-01-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200122_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportedlanguages',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
