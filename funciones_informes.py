def listar_por_criterio(lista,criterio):
    mostrar_encabezado("----------------------")
    mostrar_encabezado(f"**{criterio.upper()}**")
    mostrar_encabezado("----------------------")
    
    for heroe in lista:
        mostrar_heroe_criterio(heroe,criterio)
def mostrar_heroe_criterio(heroe, criterio):
    
    print (heroe[criterio])
def listar_por_criterio(lista,criterio):
    mostrar_encabezado("----------------------")
    mostrar_encabezado(f"**{criterio.upper()}**")
    mostrar_encabezado("----------------------")

    for heroe in lista:
        mostrar_heroe_criterio(heroe,criterio)
def mostrar_encabezado(mensaje):
    print(mensaje)
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