# Generated by Django 4.2.9 on 2024-02-18 21:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taivin_cms", "0015_articles_counter_color_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="color",
            name="color",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Цвет текста"
            ),
        ),
    ]
