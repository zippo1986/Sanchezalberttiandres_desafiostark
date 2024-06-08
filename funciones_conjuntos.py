def obtener_set(lista:list, atributo:str):
    set_datos= set()

    for i in lista:
        set_datos.add(i[f"{atributo}"])
    
    return set_datos
def agrupar_conjuntos (lista_personajes, set_datos, atributo):
#agrupar_conjuntos
#Esta funcion toma una lista de personajes toma una lista de datos y un atributo
#itera por el set de datos que es un set convertido a lista en la misma llamada
# recorre la lista de personajes y compara 
# Luego agrega los nombres de los personajes cuyos valores del atributo pasado por
# parametro y son iguales, a una lista
#Es una función completamente reutilizable
    nombres= []
    for i in set_datos:
        print("*" *133)
        print(i)
        print("*" *133)
        for j in lista_personajes:
            if j[f"{atributo}"] == i:
                mostrar_heroe(j)
                  
#data                
                
                
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