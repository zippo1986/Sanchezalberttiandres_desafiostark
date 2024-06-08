
from funciones_informes import *
def obtener_set(lista:list, atributo:str):
    set_datos= set()

    for i in lista:
        set_datos.add(i[f"{atributo}"])
    
    return set_datos
def agrupar_conjuntos (lista_personajes, set_datos, atributo):
    """Agrupa conjuntos por un set de datos y un atributo

    Args:
        lista_personajes (list): lista de personajes
        set_datos (set): set de valores unicos  de datos
        atributo (str):  la clave por la cual se quiere agrupar los datos
    """
    nombres= []
    for i in set_datos:
        print("*" *133)
        print(i)
        print("*" *133)
        for j in lista_personajes:
            if j[f"{atributo}"] == i:
                mostrar_heroe(j)
                  
                
                
                
def obtener_cantidades(lista_heroes:list,atributo:str ):
    """obtiene cantidades por marca

    Args:
        lista_ins (list): lista de diccionarios de insumos
        lista_cat (list): lista de categorias
        atributo (str):clave
    """
    lista_cat = obtener_set(lista_heroes, atributo)
    contador = 0
    print("*"*20)
    print(f"{atributo}       Cantidad")
    print("*"*20)
    for i in lista_cat:
        for heroe in lista_heroes :
            if heroe[atributo] == i:
                contador = contador+1
        
        print(f"{i:<16} {contador:<4}")
        
        contador =0