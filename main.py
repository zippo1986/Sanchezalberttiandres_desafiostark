from data_stark import lista_personajes
from funciones import *
for elemento in lista_personajes:
    print(elemento.keys())
listar_por_criterio(lista_personajes)
mostrar_por_doscriterios(lista_personajes,"nombre","altura")


