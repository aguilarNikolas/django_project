# Generated by Django 5.1.5 on 2025-02-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_outlet", "0003_alter_book_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(blank=True, default=""),
        ),
    ]
