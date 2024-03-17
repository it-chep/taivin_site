from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from taivin_cms.admin import admin_site
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = ([
    path("admin/", admin_site.urls),
    path("", include("taivin_cms.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
