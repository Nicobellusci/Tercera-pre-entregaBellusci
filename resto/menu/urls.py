from django.urls import path, include
from menu.views import *

urlpatterns = [
    path('', home, name="Home"),
    path('Entradas/', entradas, name="Entradas"),
    path('Burgers/', burgers, name="Burgers"),
    path('Pizzas/', pizzas, name="Pizzas"),
    path('Empanadas/', empanadas, name="Empanadas"),

    path('Acerca/', acerca, name="Acerca"),


    #_____FORMULARIOS_____
    path('EntradasForm/', entradasForm, name="EntradasForm"), #resuelve entradasForm y la clave el name="EntradasForm" que podria poner en un href para referanciar este link.
    path('PizzasForm/', pizzasForm, name="PizzasForm"),
    path('BurgersForm/', burgersForm, name="BurgersForm"),
    path('EmpanadasForm/', empanadasForm, name="EmpanadasForm"),

    #___________________________

    #_____BUSCAR_____
    path('buscarEntradas/', buscarEntradas, name="buscarEntradas"),
    path('encontrarEntradas/', encontrarEntradas, name="encontrarEntradas"),


]