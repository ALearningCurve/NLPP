# Generated by Django 3.0 on 2020-05-29 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20200529_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmemberinteractioninformation',
            name='post_member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_information', to='posts.PostMembers'),
        ),
    ]