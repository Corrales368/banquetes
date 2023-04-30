from django.urls import path

from apps.banquets import views

app_name = "banquets"

urlpatterns = [
    path("banquetes/", views.BanquetsTemplateView.as_view(), name="banquets-list"),
]
