# Generated by Django 3.0 on 2020-05-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20200311_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmembers',
            name='has_completed_work',
            field=models.BooleanField(default=False),
        ),
    ]
