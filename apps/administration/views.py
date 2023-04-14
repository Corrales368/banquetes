from django.views.generic import (
    ListView
)

from apps.customers.models import Customer


class CustomersListView(ListView):
    template_name = 'administration/customers/list.html'
    model = Customer
    context_object_name = 'customers'
    paginate_by = 10
