from django.urls import path
from Tienda.views import *

urlpatterns = [
    path("inicio/", vista_inicio, name = "Tienda-inicio"),
    path("registro/", vista_registro, name = "Tienda-registro"),
    path("juego/", vista_juego, name = "Tienda-juego"),
    path("consola/", vista_consola, name="Tienda-consola"),
    path("iniciar_sesion/", vista_inicio_sesion, name="Tienda-iniciar-sesion"),
    path("busqueda/", vista_busqueda, name="Tienda-busqueda"),
    path("resultado_busqueda/", vista_resultado, name="Tienda-busqueda-resultado")

]