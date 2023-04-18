from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView
)

from apps.customers.models import Customer


class CustomersListView(ListView):
    template_name = 'administration/customers/list.html'
    model = Customer
    context_object_name = 'customers'
    paginate_by = 10


class CustomerDetailView(DetailView):
    template_name = 'administration/customers/detail.html'
    model = Customer
    context_object_name = 'customer'
