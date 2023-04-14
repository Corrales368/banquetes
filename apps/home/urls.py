from django.urls import path
from apps.home import views


urlpatterns = [
    path('', views.HomeLandingTemplateView.as_view(), name="home-landing")
]
