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
    print(f"El promedio de peso de los superheroes {round(promedio,2)}")


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
def mostrar_criterio_heroe(heroe,criterio):
    print(heroe[criterio])
    
def mostrar_criterio_heroes(lista,criterio):
    for heroe in lista:
        mostrar_criterio_heroe(heroe,criterio)
        
    

def menu_opcion():
    """Ejecuta el menu

    Args:
        opcion (str): esun str numerico que sirve para matchear el menu
    """
    confirmacion = "s"
    
    stark_normalizar_datos(lista_personajes) 
    maximo = []
    minimo = []
    mas_pesado =[]
    menos_pesado = []
    
    while confirmacion =="s":
        mostrar_encabezado("""Menu de opciones
                       1) imprimir por consola el nombre de cada superheroe
                       2) mostrar el nombre y altura de cada superheroe
                       3) determinar cual es el superheroe mas alto
                       4) determinar cual es el superheroe mas bajo
                       5)Determinar la altura promedio de los superheroes
                       6) informar el nombre de los superheroes indicados anteriormente(Maximo y minimo)
                        7)cualcular e informar cual es el superheroe mas y menos pesado
                        
                       """)
        opcion = input ("Ingrese opcion")
        
        match opcion:
            case "1":
                listar_por_criterio(lista_personajes,"nombre") 
                          
            case "2":
                
                mostrar_por_doscriterios(lista_personajes,"nombre","altura")
                
            case "3":
                calcular_maximo_dos(lista_personajes, "altura",maximo)
                
                
            case "4":
                
                calcular_minimo(lista_personajes,"altura",minimo)
                
                
            case "5":
                mostrar_prom(lista_personajes, "altura")
                
            case "6":
                
                listar_por_criterio(maximo,"nombre")
                listar_por_criterio(minimo,"nombre")
            case "7":
                calcular_maximo_dos(lista_personajes,"peso",mas_pesado)
                calcular_minimo(lista_personajes,"peso",menos_pesado)
                listar_heroes(mas_pesado)
                listar_heroes(menos_pesado)
                
                

        confirmacion= input("Desea realizar otra operacion? s/n")