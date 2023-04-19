from django.urls import path

from users.views import login, registration, profile

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile")
]

app_name = "users"
