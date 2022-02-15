from django.shortcuts            import render
from django.views.generic 		 import ListView, CreateView
from django.urls          		 import reverse_lazy
from .models                     import Usuario
from .forms                      import UsuarioForm

class Registrarme(CreateView):
    template_name = "usuario/registrar.html"
    model= Usuario
    form_class = UsuarioForm

