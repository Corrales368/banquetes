from django.views.generic import ListView

from apps.users.models import LoginActivity


class LoginActivityListView(ListView):
    model = LoginActivity
    template_name = "users/login_activity_list.html"
    context_object_name = "login_activity_list"
    paginate_by = 10
    ordering = "-date_login"
    queryset = LoginActivity.objects.all()

    
    