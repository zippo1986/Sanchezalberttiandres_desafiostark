#1 normalizar datos
from data_stark import *
bandera = False

#Bibliotecas
#biblioteca validaciones
def stark_normalizar_datos(lista_heroes):
    """_summary_
    # Valida que la lista de héroes no esté vacía
    #Inicializa la inteligencia vacio con "No tiene"
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
        
        if i["inteligencia"] == "":
            i["inteligencia"] = "No tiene"
        
                    
    if modificado:
        print("Datos normalizados")
def validar_opcion(opcion):
    """Valida rango de opcion

    Args:
        opcion (str): opcion elegida

    Returns:
        bool: retorna un booleano que define si entra al menu o no
    """
    retorno = False
    if not ((int(opcion) > 15) or (int(opcion) <= 0)):
        retorno = True
    
    return retorno
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
def calcular_minimo(lista, atributo_uno,lista_minimo):
    """Calcula los  minimos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el minimo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del minimo en determinado atributo
    """
    bandera = True
    numero_minimo = None
    
    # lista para almacenar múltiples elementos máximos
    for i in lista:
        if  (bandera ==True)or(float(i[atributo_uno]) <(numero_minimo)) :
            
            numero_minimo =float(i[atributo_uno])
            bandera= False
    
    for i in lista:
        if float(i[atributo_uno])== numero_minimo:
            lista_minimo.append(i)            

def validar_opcion(opcion):
    """Valida rango de opcion

    Args:
        opcion (str): opcion elegida

    Returns:
        bool: retorna un booleano que define si entra al menu o no
    """
    retorno = False
    if not ((int(opcion) > 7) or (int(opcion) <= 0)):
        retorno = True
    
    return retorno    

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
    
        
def validar_opcion(opcion):
    """Valida rango de opcion

    Args:
        opcion (str): opcion elegida

    Returns:
        bool: retorna un booleano que define si entra al menu o no
    """
    retorno = False
    if not ((int(opcion) > 15) or (int(opcion) <= 0)):
        retorno = True
    
    return retorno







  
    

            

    
#Biblioteca ejecucion programa

    
     


#Biblioteca menu#
def menu():
    """
    Muestra el menu
    """
    print("""
1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
2. Recorrer la lista imprimiendo por consola el nombre de cada superheroe de genero F
3. Recorrer la lista y determinar cuál es el superhéroe más alto del género M
4. Recorrer la lista y determinar cuál es el superhéroe más alto del género F
5. Recorrer la lista y determinar cuál es el superhéroe más bajo del género M
6. Recorrer la lista y determinar cual es el superheroe mas bajo del género F
7. Recorrer la lista y determinar la altura promedio de los superheros de genero M
8. Recorrer la lista y determinar la altura promedio de los superheroes de genero 
9. informar el Nombre del superheroe asociado a cada uno de los indicadores anteriores (Items C a F)
10. Determinar cuantos duperheroes tienen cada tipo de color de ojos
11. Determinar cuantos duperheroes tienen cada tipo de color de pelo
12. Determinar cuantos superheroes tienen cada tipo de inteligencia (En caso de no tener inicializarlo con "No tiene")
13. listar todos los superheroes agrupados por color de ojos
14. Listar todos los superheroes por color de pelo
15.Listar todos los superhéroes agrupados por tipo de inteligencia""")
    
