from django.contrib import admin
from django.urls import path
from taivin_cms.views import *

from django.views.decorators.cache import cache_page


urlpatterns = [
    path("", cache_page(60 * 60 * 4)(MainPageView.as_view()), name="main_page"),
    path("presentations/", PresentationListView.as_view(), name="presentations"),
    path("presentations/<slug:slug_name>/", cache_page(60 * 60 * 4)(PresentationDetailView.as_view()), name="presentation_detail"),
    path('get_font/<int:font_id>/', get_font, name='get_font'),
]