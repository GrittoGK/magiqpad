# Generated by Django 4.1.1 on 2022-09-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="story_characters",
        ),
        migrations.RemoveField(
            model_name="project",
            name="story_json",
        ),
        migrations.AddField(
            model_name="project",
            name="body",
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="characters",
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="is_reading_mode",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="project",
            name="stories",
            field=models.JSONField(default=dict, null=True),
        ),
    ]
