from django.shortcuts import render
from apps.productos.models import Producto

def inicio(request):
	productos = Producto.objects.all()

	usuario = {
		"nombre": "Ludmila",
		"apellido": "Ceriani"
	}

	context = {
		"usuario": usuario,
		"productos": productos
	}
	return render(request,"inicio.html", context)

def login(request):
	return render(request,"login.html")




