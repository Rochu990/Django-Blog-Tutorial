# Generated by Django 5.0.4 on 2024-05-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="snippet",
            field=models.CharField(
                default="Click Link Above To Read Blog Post.", max_length=255
            ),
        ),
    ]
