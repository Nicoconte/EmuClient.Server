from django.urls import path

from .views import *

urlpatterns = [
    path('generate/', generate_license_key)
]
