# Generated by Django 4.1 on 2023-03-28 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_goals_time_alter_goals_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goals',
            name='user',
        ),
        migrations.CreateModel(
            name='UserGoals',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('goals', models.ManyToManyField(related_name='user_goals', to='accounts.goals')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
