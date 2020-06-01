# Generated by Django 3.0 on 2020-05-29 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0018_postmembers_has_completed_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='users',
        ),
        migrations.AlterField(
            model_name='postmembers',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_asignees', to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='postmembers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PostMemberInteractionInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_clicks', models.TextField(default='{"1": []}')),
                ('double_clicks', models.TextField(default='{"1": []}')),
                ('post_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_information', to='posts.PostMembers')),
            ],
        ),
    ]