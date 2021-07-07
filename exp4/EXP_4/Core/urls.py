from django.urls import path
from .views import Ver, index, login, registroo

urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('registroo', registroo, name="registroo"),
    path('ver', Ver, name="ver")
]