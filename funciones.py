from data_stark import lista_personajes

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
        
def mostrar_por_doscriterios(lista,criterio_uno,criterio_dos):
    mostrar_encabezado("------------------------------------------------")
    mostrar_encabezado(f"{criterio_uno}                 {criterio_dos}")
    mostrar_encabezado("------------------------------------------------")
    
    for diccionario in lista:
        
        print(f"|{diccionario[criterio_uno]:19} | {diccionario[criterio_dos]:20}|")
def mostrar_heroe_criterio(heroe, criterio):
    
    print (heroe[criterio])
def listar_por_criterio(lista,criterio):
    for heroe in lista:
        mostrar_heroe_criterio(heroe,criterio)

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

def validar_opcion(opcion):
    """Valida rango de opcion

    Args:
        opcion (str): opcion elegida

    Returns:
        bool: retorna un booleano que define si entra al menu o no
    """
    retorno = False
    if not ((int(opcion) > 6) or (int(opcion) <= 0)):
        retorno = True
    
    return retorno
def calcular_maximo_dos(lista, atributo):
    """Calcula los  maximos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el maximo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del maximo en determinado atributo
    """
    bandera = True
    numero_maximo = None
    nombre_fuerza_maximo=[]
    # lista para almacenar múltiples elementos máximos
    for i in lista:
        if  (bandera ==True)or(float(i[atributo]) >(numero_maximo)) :
            
            numero_maximo =float(i[atributo])
            bandera= False
    
    for i in lista:
        if float(i[atributo])== numero_maximo:
            nombre_fuerza_maximo.append(i)
    return nombre_fuerza_maximo

def calcular_promedio(lista, atributo_uno):
    """Calcula promedio de dos claves de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo_uno (str): una clave del diccionario
        valor_uno (str): el valor del atributo_uno (Femenino/masculino) en este caso
        atributo_dos (str): una clave del diccionario

    Returns:
        float: promedio 
    """
    acumulador = 0
    promedio = 0
    contador = len(lista)
    

    for i in lista:
        acumulador = acumulador + i[atributo_uno]

    promedio = acumulador/contador
    return (promedio)

def mostrar_prom(lista,atributo_uno):
    """Muestra el promedio

    Args:
        lista (list): lista de heroes
        atributo_uno (str): clave del dict
        valor_uno (str): valor de la clave
        atributo_dos (str): clave del dict
    """
    promedio =calcular_promedio(lista,atributo_uno)
    print(f"El promedio de peso de los superheroes masculinos es {round(promedio,2)}")


def calcular_minimo(lista, atributo_uno):
    """Calcula los  minimos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el minimo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del minimo en determinado atributo
    """
    bandera = True
    numero_minimo = None
    nombre_fuerza_minimo=[]
    # lista para almacenar múltiples elementos máximos
    for i in lista:
        if  (bandera ==True)or(float(i[atributo_uno]) <(numero_minimo)) :
            
            numero_minimo =float(i[atributo_uno])
            bandera= False
    
    for i in lista:
        if float(i[atributo_uno])== numero_minimo:
            nombre_fuerza_minimo.append(i)
            
  
    return nombre_fuerza_minimo


def encontrar_mostrar_maximos_minimos(lista:list,operacion):

    """
    muestra los maximos o los minimos segun la operacio0n necesaria
    Args:
        lista (list): lista de heroes
        operacion (str): si necesito mostrar el maximo ">" si necesito mostrar los
    """
    
    match operacion:
        case ">":
                maximos = calcular_maximo_dos(lista,"fuerza")
                mostrar_maximos_minimos(maximos,"identidad","peso")
        case "<":
                minimo = (calcular_minimo(lista_personajes,"altura"))
                mostrar_maximos_minimos(minimo,"identidad", "nombre")

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

def mostrar_encabezado(mensaje):
    print(mensaje)  

def menu_opcion(opcion):
    """Ejecuta el menu

    Args:
        opcion (str): esun str numerico que sirve para matchear el menu
    """
    stark_normalizar_datos(lista_personajes) 
    
    bandera = False
    while (es_numero(opcion)) and (validar_opcion(opcion)) :
        match opcion:
            case "1":
                listar_por_criterio(lista_personajes,"nombre") 
                break          
            case "2":
                
                mostrar_por_doscriterios(lista_personajes,"nombre","altura")
                break
            case "3":
                heroe=calcular_maximo_dos(lista_personajes, "altura")
                print(heroe)
                break
            case "4":
                heroe = calcular_minimo(lista_personajes,"altura")
                print(heroe)
                break
            case "5":
                
                break