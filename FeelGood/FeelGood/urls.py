
from django.contrib import admin
from django.urls import path
from Modulos.CitasMedicas.views import FormularioContacto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FormularioContacto, name='home'),  # Redirige la ruta raíz a FormularioContacto
]