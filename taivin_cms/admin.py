from django.contrib import admin
from taivin_cms.models import *
from django.contrib.admin import AdminSite
from .admin_actions import clear_cache
from django.urls import path


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
    list_display = ('id',)


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


class MyAdminSite(AdminSite):
    index_template = 'admin/index.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('clear-cache/', clear_cache, name='clear-cache'),
        ]
        return custom_urls + urls


admin_site = MyAdminSite(name='myadmin')

admin_site.register(Presentations, PresentationAdmin)
admin_site.register(Slides, SlideAdmin)
admin_site.register(Arts, ArtsAdmin)
admin_site.register(Creatives, CreativeAdmin)
admin_site.register(Customers, CustomerAdmin)
admin_site.register(Banners, BannerAdmin)
admin_site.register(Previews, PreviewAdmin)
