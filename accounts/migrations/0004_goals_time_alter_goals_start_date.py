# Generated by Django 4.1 on 2023-03-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_goals'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='goals',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
