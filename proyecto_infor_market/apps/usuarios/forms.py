from django       import forms
from .models      import Usuario
from django.forms import ModelForm
from datetime     import datetime

class UsuarioForm(forms.ModelForm):
	titulo = forms.CharField(label="Nombre del Usuario", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Por favor ingrese nombre"}))
	imagen=forms.CharField(label="Fotografía URL", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese la URL foto"}))

	class Meta:
		model = Usuario
		fields = ["password", "username", "first_name", "last_name", "email"]