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
    
   
    for i in lista:
        if  (bandera ==True)or((i[atributo]) >(numero_maximo)) :
            
            numero_maximo =(i[atributo])
            bandera= False
    
    for i in lista:
        if (i[atributo])== numero_maximo:
            lista_maximo.append(i)