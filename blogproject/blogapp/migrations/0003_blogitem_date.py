# Generated by Django 2.2.6 on 2019-10-08 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20191008_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogitem',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
