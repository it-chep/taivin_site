from django.db import models
from django.conf import settings
from model_utils import Choices


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

    banner_type = models.IntegerField(choices=BANNERS_TYPES, default=BANNERS_TYPES.horizontal, verbose_name="Вид баннера")
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
    chapter = models.CharField(verbose_name="Раздел", max_length=255)
    size = models.CharField(verbose_name="Размер", max_length=255)
    position = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def __str__(self):
        ...


class Fonts(models.Model):
    ...


class Colors(models.Model):
    ...


class Articles(models.Model):
    ...


