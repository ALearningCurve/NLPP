# Generated by Django 3.0.7 on 2020-06-11 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_post_clicks_to_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmembers',
            name='completion_date',
            field=models.DateTimeField(null=True),
        ),
    ]
