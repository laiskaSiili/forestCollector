# Generated by Django 2.2.1 on 2019-05-23 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forestcollector', '0002_standinformation_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standinformation',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
