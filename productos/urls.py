from django.urls import path
from . import views
#/productos
app_name = 'productos'
urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path(
        '<int:producto_id>',
        views.detalle,
        name='detalle'
    ),
]