from django.shortcuts import render
from menu.models import *
from menu.forms import *


# Create your views here.
def home(request):
    return render(request, "menu/home.html") #cambie el index por home para poder hacer distinta la pagina inicial, del index se llevan los demas html.

def entradas(request):
    contexto = {"Entradas": Entradas.objects.all()}
    return render(request, "menu/Entradas.html", contexto)

def burgers(request):
    contexto = {"Burgers": Burger.objects.all()}
    return render(request, "menu/Burgers.html", contexto)

def pizzas(request):
    contexto = {"Pizzas": Pizza.objects.all()}
    return render(request, "menu/Pizzas.html", contexto)

def empanadas(request):
    contexto = {"Empanadas": Empanadas.objects.all()}
    return render(request, "menu/Empanadas.html", contexto)

def acerca(request):
    return render(request, "menu/Acerca.html")

#_____FORMULARIOS_____
#_____Entradas:
def entradasForm(request):
    if request.method == "POST": #pregunto si el requerimiento es POST (osea si ya vienen los datos cargados).
        miForm = EntradasForm(request.POST)
        if miForm.is_valid():
            entradas_nombre = miForm.cleaned_data.get("nombre")
            entradas_ingredientes = miForm.cleaned_data.get("ingredientes")
            entradas = Entradas(nombre=entradas_nombre, ingredientes=entradas_ingredientes)
            entradas.save()
            contexto = {"Entradas": Entradas.objects.all()}
            return render(request, "menu/Entradas.html", contexto)


    else: #si es else quiere decir que es la primera vez que me piden el formulario. Entonces voy a crear un formulario vacio.
        miForm = EntradasForm() #Creo el fomulario miForm desde EntradasForm (que es la clase creada).
    
    return render(request, "menu/EntradasForm.html", {"form": miForm}) #Agrego el html que va a resolver y envio el formulario como un dicconario que va a tener como clave: "form" y como valor miForm.

#_____Pizzas:
def pizzasForm(request):
    if request.method == "POST":
        miForm = PizzasForm(request.POST)
        if miForm.is_valid():
            pizzas_nombre = miForm.cleaned_data.get("nombre")
            pizzas_ingredientes = miForm.cleaned_data.get("ingredientes")
            pizzas = Entradas(nombre=pizzas_nombre, ingredientes=pizzas_ingredientes)
            pizzas.save()
            contexto = {"Pizzas": Pizza.objects.all()}
            return render(request, "menu/Pizzas.html", contexto)

    else:
        miForm = PizzasForm()
    
    return render(request, "menu/PizzasForm.html", {"form": miForm})

#_____Burgers:
def burgersForm(request):
    if request.method == "POST":
        miForm = BurgersForm(request.POST)
        if miForm.is_valid():
            burgers_nombre = miForm.cleaned_data.get("nombre")
            burgers_ingredientes = miForm.cleaned_data.get("ingredientes")
            burgers_tipo_pan = miForm.cleaned_data.get("tipo_pan")
            burgers = Entradas(nombre=burgers_nombre, ingredientes=burgers_ingredientes, tipo_pan=burgers_tipo_pan)
            burgers.save()
            contexto = {"Burgers": Burger.objects.all()}
            return render(request, "menu/Burgers.html", contexto)

    else:
        miForm = BurgersForm()
    
    return render(request, "menu/BurgersForm.html", {"form": miForm})

#_____Empanadas:
def empanadasForm(request):
    if request.method == "POST":
        miForm = EmpanadasForm(request.POST)
        if miForm.is_valid():
            empanadas_nombre = miForm.cleaned_data.get("nombre")
            empanadas_ingredientes = miForm.cleaned_data.get("ingredientes")
            empanadas_coccion = Empanadas(nombre=empanadas_nombre, ingredientes=empanadas_ingredientes, coccion=empanadas_coccion)
            empanadas.save()
            contexto = {"Empanadas": Empanadas.objects.all()}
            return render(request, "menu/Empanadas.html", contexto)

    else:
        miForm = EmpanadasForm()
    
    return render(request, "menu/EmpanadasForm.html", {"form": miForm})

#___________________________


#_____BUSCAR_____

def buscarEntradas (request):
    return render(request, "menu/buscarEntradas.html") #renderiza un formulario buscarEntradas solo para ingresar el pataron a buscar.

def encontrarEntradas (request):
    if request.GET["buscar"]: #aplico el filtro, si viene algo en el campo name="buscar" del buscarEntradas.html <p> Ingrese el patrón de búsqueda: <input type="text" name="buscar" id="buscar"></p> .
        patron = request.GET["buscar"] #mi patron va a ser el dato ingresado
        entradas =Entradas.objects.filter(nombre__icontains=patron) #creo un obtejo entradas invocando a la class Entradas.objects.filter(), donde le digo que el nombre contenga el patron ingresado.
        contexto = {"Entradas": entradas} #devuelve todos los objetos que cumplen con el filtro.
    else:
        contexto = {"Entradas": Entradas.objects.all()} #si no se pone un patron de busqueda devuelve todas las Entradas.
    
    return render(request, "menu/Entradas.html", contexto)
