# Generated by Django 2.2 on 2020-07-14 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20200710_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetmodel',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.TweetModel'),
        ),
    ]
