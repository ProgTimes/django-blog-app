# Generated by Django 5.0.6 on 2024-07-08 20:20

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_post_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["title"], "verbose_name_plural": "categories"},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="title", unique=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="blog.post"
            ),
        ),
    ]