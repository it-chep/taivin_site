# Generated by Django 4.2.9 on 2024-02-17 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taivin_cms", "0011_alter_slides_chapter_alter_slides_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="presentations",
            name="about_customer",
            field=models.TextField(blank=True, null=True, verbose_name="О заказчике"),
        ),
        migrations.CreateModel(
            name="AdditionalBenefits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.TextField(blank=True, null=True, verbose_name="Доп текст"),
                ),
                (
                    "position",
                    models.PositiveSmallIntegerField(
                        default=1, verbose_name="Порядок сортировки"
                    ),
                ),
                (
                    "presentation",
                    models.ForeignKey(
                        blank=True,
                        help_text="Презентация",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="taivin_cms.presentations",
                        verbose_name="Презентация",
                    ),
                ),
            ],
            options={
                "verbose_name": "Дополнительные преимущества презентации",
                "verbose_name_plural": "Дополнительные преимущества презентации",
            },
        ),
    ]
