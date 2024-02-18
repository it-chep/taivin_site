from django.contrib import admin
from taivin_cms.models import *


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    class SlidesInline(admin.TabularInline):
        model = Slides
        extra = 0

    class FontsInline(admin.TabularInline):
        model = Fonts
        extra = 0

    class ColorInline(admin.TabularInline):
        model = Color
        extra = 0

    class ArticlesInline(admin.TabularInline):
        model = Articles
        extra = 0

    class AdditionalBenefitsInline(admin.TabularInline):
        model = AdditionalBenefits
        extra = 0

    inlines = [SlidesInline, FontsInline, ColorInline, ArticlesInline, AdditionalBenefitsInline]


class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', "name")


class PreviewAdmin(admin.ModelAdmin):
    list_display = ('id', "name")


class ArtsAdmin(admin.ModelAdmin):
    list_display = ('id', "name")


class CreativeAdmin(admin.ModelAdmin):
    list_display = ('id', "name")


admin.site.register(Presentations, PresentationAdmin)
admin.site.register(Slides, SlideAdmin)
admin.site.register(Arts, ArtsAdmin)
admin.site.register(Creatives, CreativeAdmin)
admin.site.register(Customers, CustomerAdmin)
admin.site.register(Banners, BannerAdmin)
admin.site.register(Previews, PreviewAdmin)


