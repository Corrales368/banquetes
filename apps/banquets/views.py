from django.views.generic import TemplateView


class BanquetsTemplateView(TemplateView):
    template_name = "banquets/banquets_list.html"
