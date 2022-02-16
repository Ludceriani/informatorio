from django       import forms
from .models      import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
	username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre de usuario"}))
	first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre"}))
	last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese apellido"}))
	#password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = Usuario
		fields = ["username", "first_name", "last_name", "email"]