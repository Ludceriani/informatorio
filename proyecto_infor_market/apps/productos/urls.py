from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
	path("Detalle/", views.detalle, name="detalle")
]