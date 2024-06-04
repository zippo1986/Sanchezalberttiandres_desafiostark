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
def listar_por_criterio(lista):
    for heroe in lista:
        mostrar_heroe_criterio(heroe,"nombre")

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
    bandera = False
    while (es_numero(opcion)) and (validar_opcion(opcion)) :
        match opcion:
            case "1":
                stark_normalizar_datos(lista_personajes) 
                bandera = True
                break          
            case "2":
                
                listar_por_criterio(lista_personajes,"nombre")
                break
            case "3":
                encontrar_mostrar_maximos_minimos(lista_personajes, "<")
                break
            case "4":
                mostrar_prom(lista_personajes,"genero", "M", "peso")
                break
            case "5":
                mostrar_mayores_promedio(lista_personajes)
                break
            case "6":
                exit()