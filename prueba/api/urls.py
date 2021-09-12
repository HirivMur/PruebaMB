from django.conf.urls import url
from django.urls import path
from api.views import API_Usuario, API_delete_update, Usuario_alfabetico, Usuario_edad


urlpatterns = [
	url(r'^v0/usuario/$', API_Usuario.as_view()),
	path('v0/usuario/<int:id>', API_delete_update.as_view()),
	url(r'^v0/usuario/alfabeticamente', Usuario_alfabetico.as_view()),
    url(r'^v0/usuario/edad', Usuario_edad.as_view()),
]