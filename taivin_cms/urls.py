from django.contrib import admin
from django.urls import path
from taivin_cms.views import *

urlpatterns = [
    path("", MainPageView.as_view(), name="main_page"),
    path("presentations/", PresentationListView.as_view(), name="presentations"),
    path("presentations/<slug:slug_name>/", PresentationDetailView.as_view(), name="presentation_detail")
    # path("/previews/<slug:slug_name>/", PresentationDetailView, name="presentations")
    # path("/websites/<slug:slug_name>/", PresentationDetailView, name="presentations")
    # path("/creatives/<slug:slug_name>/", PresentationDetailView, name="presentations")
    # path("/banners/<slug:slug_name>/", PresentationDetailView, name="presentations")
]