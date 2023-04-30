from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)

from apps.customers.models import Customer


class CustomersListView(LoginRequiredMixin,ListView):
    template_name = "administration/customers/list.html"
    model = Customer
    context_object_name = "customers"
    paginate_by = 10


class CustomerDetailView(LoginRequiredMixin,DetailView):
    template_name = "administration/customers/detail.html"
    model = Customer
    context_object_name = "customer"
