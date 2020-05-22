# Generated by Django 3.0.6 on 2020-05-21 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200521_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgroup',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
    ]