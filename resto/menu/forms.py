from django import forms #modulo que para crear formularios y contienen clases como los models.


#_____CLASES FORM_____
#_____Entradas:
class EntradasForm(forms.Form): #este formulario va a tener los datos que le voy a pedir al usuario.
    nombre = forms.CharField(max_length=50, required=True) #como este dato es obligario le agrego el requerido=True
    ingredientes = forms.CharField(max_length=100, required=True)

#_____Pizzas:
class PizzasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    ingredientes = forms.CharField(max_length=100, required=True)

#_____Burgers:
class BurgersForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    ingredientes = forms.CharField(max_length=100, required=True)
    tipo_pan = forms.CharField(max_length=50, required=True)

#_____Empanadas:
class EmpanadasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    ingredientes = forms.CharField(max_length=100, required=True)
    coccion = forms.CharField(max_length=50, required=True)