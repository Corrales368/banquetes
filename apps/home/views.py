from django.views.generic import TemplateView


class HomeLandingTemplateView(TemplateView):
    template_name = "home/landing/landing.html"
