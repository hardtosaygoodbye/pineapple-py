# Generated by Django 2.1.7 on 2019-05-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userInfo', '0004_auto_20190522_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='QQ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='wechat',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='微信号'),
        ),
    ]
