# Generated by Django 3.0 on 2020-01-23 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20200122_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='from_lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_langs', to='posts.SupportedLanguages'),
        ),
        migrations.AlterField(
            model_name='post',
            name='to_lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_langs', to='posts.SupportedLanguages'),
        ),
    ]
