# Generated by Django 2.1.7 on 2019-05-15 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=100, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=20, verbose_name='话题')),
                ('content', models.TextField(max_length=200, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='FeedImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField()),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Feed')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Feed'),
        ),
        migrations.AddField(
            model_name='comment',
            name='fromUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='userInfo.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='toUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='userInfo.User'),
        ),
    ]