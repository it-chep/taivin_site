# Generated by Django 4.2.9 on 2024-01-30 23:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taivin_cms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="presentations",
            name="name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
