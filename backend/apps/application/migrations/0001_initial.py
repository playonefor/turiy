# Generated by Django 3.0.6 on 2020-05-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='应用名称')),
                ('env', models.CharField(choices=[(0, '开发环境'), (1, '测试环境'), (2, 'beta环境'), (3, '生产环境')], max_length=20, verbose_name='环境')),
                ('comment', models.CharField(max_length=1000, verbose_name='备注')),
            ],
            options={
                'verbose_name': '应用',
                'verbose_name_plural': '应用',
                'ordering': ('name',),
            },
        ),
    ]
