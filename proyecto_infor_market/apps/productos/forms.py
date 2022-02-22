from django       import forms
from .models      import Producto
from django.forms import ModelForm
from datetime     import datetime

class ProductoForm(forms.ModelForm):
	titulo = forms.CharField(label="Nombre del producto", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Por favor ingrese nombre"}))
	imagen = forms.CharField(label="Fotografía URL", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese la URL foto"}))

	class Meta:
		model = Producto
		fields = ["nombre", "precio", "imagen"]
	

"""class DateInput(forms.DateInput):
    input_type='date'"""