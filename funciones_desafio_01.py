#1 normalizar datos
from data_stark import *
bandera = False

#Bibliotecas
#biblioteca validaciones
def stark_normalizar_datos(lista_heroes):
    """_summary_
    # Valida que la lista de héroes no esté vacía
    
    # Recorre la lista de héroes
    # Recorre las keys de cada héroe
    # Valida que la key represente un dato numérico y que no sea None
    # Convierte el tipo de dato y marca como modificado
    Args:
        lista_heroes (_type_): _description_
    """
    
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return
    modificado = False

    tipos_dato = {"edad": int, "altura": float, "peso": float, "fuerza": int}
    for heroe in lista_heroes:
        for key in heroe:
            if key in tipos_dato and heroe[key] is not None:
                
                if type(heroe[key]) != tipos_dato[key]:
                    
                    heroe[key] = tipos_dato[key](heroe[key])
                    modificado = True
    for i in lista_heroes:
        if i["color_ojos"] == "Yellow (without irises)":
            i["color_ojos"] = "Yellow2"
        if i["color_pelo"] == "Red / Orange":
            i["color_pelo"] = "R/0"
        elif i["color_pelo"] == "Brown / White":
            i["color_pelo"] = "B/W"
                    
    if modificado:
        print("Datos normalizados")
def validar_entero(numero:str):
    """_summary_
    Valida que el numero pasado por str sea enttero

    Args:
        numero (str): recibe un numero en str

    Returns:
        _type_: retorna true o false
    """
    for i in numero:
        try:
            int(i)
            return True
        except ValueError:
            return False
def es_numero(cadena:str):
    """Valida que un str sea un valor numerico

    Args:
        cadena (str): caracter numerico

    Returns:
        bool: retorna un booleano
    """
    try:
        int(cadena)
        return True
    except ValueError:
        
        return False

#Biblioteca manipulacion de datos
def obtener_dato(heroe:dict, key: str):
    """_summary_
    toma un diccionario y una clave y obtiene la clave y el valor de la clave "nombre" y otra clave (pasada por parametro) y su valor 
    Args:
        heroe (dict): diccionario
        key (str):string
    """
    retorno = False
    tipos_dato = ["nombre","altura","fuerza", "peso", "identidad", "inteligencia","genero"]
    
    if key  in tipos_dato and key is not None:
        retorno = heroe[key]
        
    return retorno


def obtener_nombre(heroe:dict):
    """_summary_
    toma un diccionario y una clave y obtiene la clave y el valor de la clave "nombre" y otra clave (pasada por parametro) y su valor 
    Args:
        heroe (dict): diccionario
        key (str):string
    """

    retorno = False
    if heroe is not None:
        retorno = f"nombre: {obtener_dato(heroe, 'nombre')}"
    return retorno
#2
def obtener_nombre_y_dato(heroe:dict, key: str):
    """_summary_
    toma un diccionario y una clave y obtiene la clave y el valor de la clave "nombre" y otra clave (pasada por parametro) y su valor 
    Args:
        heroe (dict): diccionario
        key (str):string
    """
    retorno = False
    nombre = obtener_nombre(heroe)
    dato = obtener_dato(heroe,key)
    if (nombre) and (dato):
        retorno = f"Nombre: {heroe['nombre']}| {dato} {heroe[dato]}"

    return retorno
def obtener_dato_cantidad(lista,numero,key):
    lista_heroes_cantidad =[]
    for i in lista:
        if (i[key])== numero:
            lista_heroes_cantidad.append(i)
    return lista_heroes_cantidad
#Biblioteca calculos
def calcular_maximo(lista, atributo):
    """Calcula los  maximos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el maximo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del maximo en determinado atributo
    """
    bandera = True
    numero_maximo = None
    
    if lista is not None and atributo is not None:
    # lista para almacenar múltiples elementos máximos
        for i in lista:
            if  (bandera ==True)or((i[atributo]) >(numero_maximo)) :
                numero_maximo =(i[atributo])
                bandera= False
        
    return numero_maximo

def sumar_dato_heroe(lista:list, key: str):
    """_summary_
    suma los datos de una clave de todos los heroes
    Args:
        lista (list):lista
        key (str): clave de un diccionario

    Returns:
        _type_: _description_
    """
    suma = 0 
    for heroe in lista:
        if type(heroe) == dict and heroe is not None:
            
            suma = heroe[f"{key}"] + suma
    return suma

def dividir (dividendo,divisor):
    """_summary_
    divide dos numeros validando que el divisor no sea 0 
    Args:
        dividendo (_type_): un dividendo
        divisor (_type_): un divisor

    Returns:
        _type_: retorna el resultado o 0 si el valor del divisor es 0 
    """
    
    calculo = 0
    
    calculo = dividendo/divisor
    if divisor == 0:
        calculo = 0
    return calculo

def calcular_promedio_dos(lista:list, key:str):
    """_summary_
    calcula el promedio de una clave pasada por parametro, luego de recorrer unalista de diccionarios

    Args:
        lista (list): lista de superheroes
        key (str): una clave del diccionario

    Returns:
        _type_: _description_
    """
    cantidad = 0
    for i in lista:
        cantidad = cantidad + 1
    promedio = dividir(sumar_dato_heroe(lista,key), cantidad)
    return promedio
def calcular_minimo(lista, atributo_uno):
    """Calcula los  minimos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el minimo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del minimo en determinado atributo
    """
    bandera = True
    heroe_atributo_minimo =[]
    numero_minimo = None
    # lista para almacenar múltiples elementos máximos
    if lista is not None and atributo_uno is not None:
        
        for i in lista:
            if  (bandera ==True)or(int(i[atributo_uno]) <(numero_minimo)) :
                numero_minimo =(i[atributo_uno])
                bandera= False
    
    return numero_minimo            

    

def filtrar_datos(lista, valor, key,lista_filtro):
    """Filtra por valor de una determinada clave

    Args:
        lista (list): lista de elementos
        valor (str): valor a filtrar
        key (str): clave del valor a filtrar

    Returns:
        list: retorna una lista de diccionarios con los valores filtrados 
    """
    
    
    if lista and valor is not None:
        for i in lista:
            if i[key] ==valor:
                lista_filtro.append(i)
    
        
#Biblioteca mostrar datos
def listar_heroes(lista: list) -> None:
    """Realiza un listado de los heroes

    Args:
        lista (list): lista de heroes
    """
    print("***Lista de Heroes***")
    print("-------------------------------------------" *3)
    print("nombre                identidad                       empresa     altura  peso    genero  ojos    pelo      fuerza  inteligencia")
    print("-------------------------------------------" *3)
    
    # Ordenar la lista de héroes por nombre
    #lista_ordenada = sorted(lista, key=lambda heroe: heroe['nombre'])
    
    for heroe in lista:
        mostrar_heroe(heroe)
        

    print("-----------------------------------------"*3)
def mostrar_nombre(lista):
    for i in lista:
        print(i["nombre"])
def mostrar_heroe(heroe) -> None:
    """Muestra los heroes por aatributo

    Args:
        heroe (dict): diccionario de heroe
    """
    print(
        f"{heroe['nombre']:18}| "
        f"{heroe['identidad']:29}| "
        f"{heroe['empresa']:3}| "
        f"{heroe['altura']:6}|"
        f"{heroe['peso']:8}|"
        f"{heroe['genero']:6}|"
        f"{heroe['color_ojos']:8}|"
        f"{heroe['color_pelo']:8}|"
        f"{heroe['fuerza']:-8}|"
        f"{heroe['inteligencia']:13}|"
    )



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
def mostrar_encabezado(mensaje):
    print(mensaje)  
    
def calcular_maximo_dos(lista, atributo, lista_maximo):
    """Calcula los  maximos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el maximo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del maximo en determinado atributo
    """
    bandera = True
    numero_maximo = None
    
    # lista para almacenar múltiples elementos máximos
    for i in lista:
        if  (bandera ==True)or((i[atributo]) >(numero_maximo)) :
            
            numero_maximo =(i[atributo])
            bandera= False
    
    for i in lista:
        if (i[atributo])== numero_maximo:
            lista_maximo.append(i)
def mostrar_heroe_criterio(heroe, criterio):
    
    print (heroe[criterio])
def listar_por_criterio(lista,criterio):
    mostrar_encabezado("----------------------")
    mostrar_encabezado(f"**{criterio.upper()}**")
    mostrar_encabezado("----------------------")

    for heroe in lista:
        mostrar_heroe_criterio(heroe,criterio)
    
#Biblioteca ejecucion programa

    
     


#Biblioteca menu#
def menu():
    """
    Muestra el menu
    """
    print("""1. Normalizar datos (No se debe poder acceder a los otros puntos)
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia
K. Salir del programa""")
    
