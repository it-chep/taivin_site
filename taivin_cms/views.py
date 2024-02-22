from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, JsonResponse
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
        presentation = Presentations.objects.prefetch_related(
            'slides_set',
            'additionalbenefits_set',
            'color_set',
            'fonts_set',
            'articles_set',
        ).select_related('customer').filter(
            slug_name=kwargs.get('slug_name')
        ).first()

        context = {
            'page_title': f"{self.page_title} {presentation.customer.name}",
            'presentation': presentation,
            'slides': presentation.slides_set.all().order_by('position'),
            'articles': presentation.articles_set.all().order_by('position'),
            'benefits': presentation.additionalbenefits_set.all().order_by('position'),
            'colors': presentation.color_set.all().order_by('position'),
            'fonts': presentation.fonts_set.all().order_by('position')
        }
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


def get_font(request, font_id):
    font = get_object_or_404(Fonts, id=font_id)
    try:
        description_font_url = font.description_font_file.url
    except Exception:
        description_font_url = None

    try:
        font_url = font.font_file.url
    except Exception:
        font_url = None
    return JsonResponse({'font_url': font_url, 'description_font_url': description_font_url})
