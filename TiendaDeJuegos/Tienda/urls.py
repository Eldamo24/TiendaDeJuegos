from django.urls import path
from Tienda.views import *

urlpatterns = [
    path("inicio/", vista_inicio, name = "Tienda-inicio")
]