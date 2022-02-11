
from apps.productos.models import Producto
from django.views.generic.base import TemplateView

"""
#Inicio Basado en Funcion
def inicio(request):
	context = {
		"productos": Producto.objects.all()
	}
	return render(request,"inicio.html", context)
"""
class Inicio(TemplateView):
	template_name = "inicio.html"
	model = Producto
	context_object_name = "productos"

	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		context["productos"] = Producto.objects.all()
		return context
		