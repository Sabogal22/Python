from django.urls import URLPattern, path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import static

from os import name
from xml.dom.minidom import Document

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('', views.login, name='login'),

    path('contacto', views.contacto, name='contacto'),
    path('contactar',views.contactar, name='contactar'),
    
    path('motos', views.motos, name='motos'),
    path('motos/crear', views.crear, name='crear'),
    path('motos/editar', views.editar, name='editar'),
    path('motos/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 