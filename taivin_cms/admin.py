from django.contrib import admin
from taivin_cms.models import *


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


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


