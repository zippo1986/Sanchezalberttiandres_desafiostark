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