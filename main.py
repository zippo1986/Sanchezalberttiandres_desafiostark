from data_stark import lista_personajes
from funciones import *

print(len(lista_personajes))
confirmacion = "s"
while confirmacion == "s":
    opcion = input ("Ingrese opcion")
    menu_opcion(opcion)
    confirmacion = input("Desea realizar otra operacion? s/n")
    

