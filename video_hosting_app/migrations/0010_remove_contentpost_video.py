# Generated by Django 4.0.6 on 2022-08-08 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("video_hosting_app", "0009_alter_contentpost_statistics"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contentpost",
            name="video",
        ),
    ]
