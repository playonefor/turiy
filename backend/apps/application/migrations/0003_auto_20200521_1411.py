# Generated by Django 3.0.6 on 2020-05-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20200521_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='env',
            field=models.CharField(choices=[('0', '开发环境'), ('1', '测试环境'), ('2', 'beta环境'), ('3', '生产环境')], max_length=1, verbose_name='环境'),
        ),
    ]
