# Generated by Django 4.2.9 on 2024-02-17 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taivin_cms", "0009_color_delete_colors_alter_articles_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="color",
            name="presentation",
            field=models.ForeignKey(
                blank=True,
                help_text="Презентация",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="taivin_cms.presentations",
                verbose_name="Презентация",
            ),
        ),
    ]
