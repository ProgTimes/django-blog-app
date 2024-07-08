# Generated by Django 5.0.6 on 2024-07-08 20:30

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_category_options_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="title", unique=True),
        ),
    ]
