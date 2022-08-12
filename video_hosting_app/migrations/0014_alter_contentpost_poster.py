# Generated by Django 4.0.6 on 2022-08-08 18:58

from django.db import migrations, models
import video_hosting_app.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ("video_hosting_app", "0013_alter_contentpost_poster"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contentpost",
            name="poster",
            field=models.ImageField(
                storage=video_hosting_app.storage_backends.PreviewStorage, upload_to="", verbose_name="Poster"
            ),
        ),
    ]
