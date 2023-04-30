from django.urls import path

from apps.users import views

app_name = "users"


urlpatterns = [
    path("login-activity/", views.LoginActivityListView.as_view(), name="login_activity_list"),
]