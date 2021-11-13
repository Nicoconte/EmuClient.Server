from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/emuclient/license-key/', include('api.license_key.urls'))
]
