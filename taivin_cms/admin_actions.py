from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.cache import cache
from django.urls import reverse
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
import shutil
import os


@staff_member_required
def clear_cache(request):
    cache_path = settings.CACHES['default']['LOCATION']

    cache.clear()

    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
        message = "Кэш успешно очищен."
        messages.success(request, message)
    else:
        message = "Папка кэша не найдена."
        messages.warning(request, message)

    request.session['admin_clear_cache'] = message

    return HttpResponseRedirect(reverse('admin:index'))
