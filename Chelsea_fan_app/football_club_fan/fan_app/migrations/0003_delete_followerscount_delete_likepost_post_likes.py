# Generated by Django 4.2.2 on 2023-08-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fan_app', '0002_followerscount_likepost_post_created_at_post_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
