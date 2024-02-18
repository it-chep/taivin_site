import os
from django.db import models
from django.conf import settings
from model_utils import Choices


def get_upload_fonts_path(instance, filename):
    return os.path.join('fonts', 'cases', filename)


def get_upload_slides_path(instance, filename):
    # Получаем имя презентации из связанного поля presentation
    presentation_name = instance.presentation.name if instance.presentation else "Unknown Presentation"
    # Генерируем путь загрузки
    return os.path.join('presentations', presentation_name, 'slides', filename)


# TODO: добавить миксин для поля "Порядок сортировки"

class Customers(models.Model):
    name = models.CharField(verbose_name="Имя заказчика", max_length=255)
    link = models.CharField(verbose_name="Ссылка на заказчика", max_length=500)

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

    def __str__(self):
        return f"Заказчик - {self.name}"


class Presentations(models.Model):
    name = models.CharField(verbose_name="Название презентации", max_length=255)
    main_banner = models.ImageField(verbose_name="Главный баннер", upload_to='presentations/', null=True, blank=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True)
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")
    slug_name = models.SlugField(unique=True, )
    main_bg_color = models.CharField(verbose_name="Цвет на главном экране", max_length=255, null=True, blank=True)
    about_customer = models.TextField(verbose_name="О заказчике", null=True, blank=True)
    font_color_background = models.CharField(
        verbose_name="Градиент background блока со шрифтами и цветами", max_length=255,
        null=True, blank=True
    )

    class Meta:
        verbose_name = "Презентация"
        verbose_name_plural = "Презентации"

    def __str__(self):
        return f"Презентация - {self.name}"


class Banners(models.Model):
    BANNERS_TYPES = Choices(
        (1, "horizontal", "Горизонтальный"),
        (2, "vertical", "Вертикальный"),
        (3, "square", "Квадратный")
    )

    banner_type = models.IntegerField(choices=BANNERS_TYPES, default=BANNERS_TYPES.horizontal,
                                      verbose_name="Вид баннера")
    name = models.CharField(verbose_name="Название превью", max_length=255)
    banner = models.ImageField(verbose_name="Баннер", upload_to='banners/', null=True, blank=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True)
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")
    slug_name = models.SlugField(unique=True)
    color = models.CharField(verbose_name="Цвет подцветки", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return f"Баннер - {self.name}"


class Creatives(models.Model):
    name = models.CharField(verbose_name="Название Креатива", max_length=255)
    creative = models.ImageField(verbose_name="Креатив", upload_to='creatives/', null=True, blank=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True)
    slug_name = models.SlugField(unique=True)
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")
    color = models.CharField(verbose_name="Цвет подцветки", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Креатив"
        verbose_name_plural = "Креативы"

    def __str__(self):
        return f"Креатив - {self.name}"


class Websites(models.Model):
    ...


class Arts(models.Model):
    name = models.CharField(verbose_name="Название Арта", max_length=255)
    preview = models.ImageField(verbose_name="Арты", upload_to='arts/', null=True, blank=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True)
    slug_name = models.SlugField(unique=True)
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")
    color = models.CharField(verbose_name="Цвет подцветки", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Арт"
        verbose_name_plural = "Арты"

    def __str__(self):
        return f"Арты - {self.name}"


class Previews(models.Model):
    name = models.CharField(verbose_name="Название превью", max_length=255)
    preview = models.ImageField(verbose_name="Превью", upload_to='preview/', null=True, blank=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True)
    slug_name = models.SlugField(unique=True)
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")
    color = models.CharField(verbose_name="Цвет подцветки", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Превью"
        verbose_name_plural = "Превью"

    def __str__(self):
        return f"Превью - {self.name}"


class Motions(models.Model):
    ...


class Slides(models.Model):
    chapter = models.CharField(verbose_name="Раздел", max_length=255, null=True, blank=True)
    size = models.CharField(verbose_name="Размер", max_length=255, null=True, blank=True)
    slide_image = models.ImageField(verbose_name="Слайд", upload_to=get_upload_slides_path, null=True, blank=True)
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")
    presentation = models.ForeignKey(
        to=Presentations,
        help_text="Презентация",
        verbose_name="Презентация",
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def __str__(self):
        return f"Слайд презентации - {self.presentation.name}"


class Fonts(models.Model):
    FILE_FORMAT_CHOICE = (
        (1, 'otf'),
        (2, 'ttf'),
        (3, 'woff')
    )

    name = models.CharField(verbose_name="Название цвета", max_length=255)
    font_file = models.FileField(verbose_name="Шрифт файла", upload_to=get_upload_fonts_path, null=True, blank=True)
    file_format = models.PositiveSmallIntegerField(
        choices=FILE_FORMAT_CHOICE,
        default=1,
        verbose_name="Формат файла со шрифтами"
    )
    presentation = models.ForeignKey(
        to=Presentations,
        help_text="Презентация",
        verbose_name="Презентация",
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Шрифт"
        verbose_name_plural = "Шрифты"

    def __str__(self):
        return f"{self.name}"


class Color(models.Model):
    linear_gradient = models.BooleanField(verbose_name="Линейный градиент", null=True, blank=True, default=False)
    code = models.CharField(verbose_name="Код цвета", max_length=255)
    presentation = models.ForeignKey(
        to=Presentations,
        help_text="Презентация",
        verbose_name="Презентация",
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")
    color = models.CharField(verbose_name="Цвет текста", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return f"{self.code}"


class Articles(models.Model):
    header = models.TextField(verbose_name="Заголовок абзаца", null=True, blank=True)
    text = models.TextField(verbose_name="Текст абзаца", null=True, blank=True)
    presentation = models.ForeignKey(
        to=Presentations,
        help_text="Презентация",
        verbose_name="Презентация",
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")
    counter_color = models.CharField(verbose_name="Код цвета счетчика", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Абзац"
        verbose_name_plural = "Абзац"

    def __str__(self):
        return f"Абзац {self.header}"


class AdditionalBenefits(models.Model):
    text = models.TextField(verbose_name="Доп текст", null=True, blank=True)
    presentation = models.ForeignKey(
        to=Presentations,
        help_text="Презентация",
        verbose_name="Презентация",
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Дополнительные преимущества презентации"
        verbose_name_plural = "Дополнительные преимущества презентации"

    def __str__(self):
        return f"Дополнительные преимущества презентации {self.text}"
