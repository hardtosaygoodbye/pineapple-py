# Generated by Django 2.1.7 on 2019-05-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userInfo', '0005_auto_20190522_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatarUrl',
            field=models.URLField(default='', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='nickName',
            field=models.CharField(default='喵呜', max_length=20, verbose_name='用户名称'),
        ),
    ]
