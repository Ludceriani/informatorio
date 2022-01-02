from django.shortcuts     import render
from django.views.generic import ListView, CreateView
from django.urls          import reverse_lazy
from .forms 			  import ProductoForm
from .models              import Producto

def detalle(request):
	context = {}	
	return render(request, "productos/detalle.html", context)

class ListarAdmin(ListView):
	template_name="productos/admin/listar.html"
	model = Producto
	context_object_name="productos"


class NuevoAdmin(CreateView):
    template_name = "productos/admin/nuevo.html"
    model= Producto
    form_class = ProductoForm

    def get_success_url(self, **kwargs):
    	return reverse_lazy("productos:admin_listar")
