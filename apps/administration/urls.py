from django.urls import path
from apps.administration import views

app_name = "administration"

urlpatterns = [
    path("customers", views.CustomersListView.as_view(), name="customers-list"),
    path("customers/<pk>", views.CustomerDetailView.as_view(), name="customer-detail"),
]
