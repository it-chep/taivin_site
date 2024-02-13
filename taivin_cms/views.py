from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from taivin_cms.models import *


class MainPageView(TemplateView):
    template_name = "main.html"
    page_title = "Главная страницы"

    def get_context_data(self, **kwargs):
        context = {
            'page_title': self.page_title,
            'previews': Previews.objects.all().order_by("position"),
            'banners': Banners.objects.all().order_by("position"),
            'arts': Arts.objects.all().order_by("position"),
            'creatives': Creatives.objects.all().order_by("position"),
            'presentations': Presentations.objects.all().order_by("position")
        }
        return context


class PresentationDetailView(TemplateView):
    template_name = "presentations/presentation_detail.html"
    page_title = "Презентация"

    def get_context_data(self, **kwargs):
        presentation = Presentations.objects.filter(slug_name=kwargs.get('slug_name', None)).first()
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title + " " + str(presentation.customer.name)
        context['main_banner'] = presentation.main_banner
        context['customer'] = presentation.customer
        return context


class PresentationListView(ListView):
    model = Presentations
    template_name = "presentations/presentation_list.html"
    page_title = "Презентации"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title

        return context

    def get_queryset(self):
        presentations = Presentations.objects.all()
        print(presentations)
        return presentations
