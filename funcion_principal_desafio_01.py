from funciones_desafio_01 import *
def main():
    
    stark_normalizar_datos(lista_personajes)
    confirmacion = "s"
    bandera = False
    lista_femeninas = []
    lista_masculinos =[]
    
    mas_altos = []
    mas_altas=[]
    mas_bajos =[]
    mas_bajas = []
    
    
    #agregado
    
    
    while confirmacion == "s":
        menu()
        
        opcion = input ("ingrese opcion")
        while not validar_entero(opcion):
            opcion = ("Ingrese opcion")
        match opcion:
            case "1":
                
                
                filtrar_datos(lista_personajes,"M","genero",lista_masculinos)
                listar_por_criterio(lista_masculinos,"nombre")
                
                           
            case "2":
                filtrar_datos(lista_personajes,"F","genero",lista_femeninas)
                listar_por_criterio(lista_femeninas,"nombre")
            case "3":
                
                calcular_maximo_dos(lista_masculinos,"altura",mas_altos)
                listar_heroes(mas_altos)
                
                #listar_heroes(lista_fem_mas_altas)
                
            case "4":
                calcular_maximo_dos(lista_femeninas,"altura",mas_altas)
                listar_heroes(mas_altas)
                

                
            case "5":
                calcular_minimo(lista_masculinos,"altura",mas_bajos)
                listar_heroes(mas_bajos)
                
            case "6":
                calcular_minimo(lista_femeninas,"altura",mas_bajas)
                listar_heroes(mas_bajas)
                    
            case "7":
                   
                promedio_altura_m = calcular_promedio_dos(lista_masculinos,"altura")
                mostrar_encabezado(f"La altura promedio de los superheroes masculinos es: {round(promedio_altura_m)}")
                    
            case "8":
                 promedio_altura_f = calcular_promedio_dos(lista_femeninas,"altura")
                 mostrar_encabezado(f"La altura promedio de los superheroes masculinos es: {round(promedio_altura_m)}")
                
            case "9":
                
                listar_por_criterio(mas_altos,"nombre")
                listar_por_criterio(mas_altas,"nombre")
                listar_por_criterio(mas_bajos,"nombre")
                listar_por_criterio(mas_bajas,"nombre")
                
                
                
            
                
            case "10":
                obtener_cantidades(lista_personajes,"color_ojos")
                
                
                
            case "11":
                obtener_cantidades(lista_personajes,"color_pelo")
                
                    
            case "12":
                obtener_cantidades(lista_personajes,"inteligencia")
                
                
                
                
            case "13":
                
                agrupar_conjuntos(lista_personajes,obtener_set(lista_personajes,"color_ojos"),"color_ojos")
                
                    
            case "14":
                agrupar_conjuntos(lista_personajes,obtener_set(lista_personajes,"color_pelo"),"color_pelo")
            case "15":
                agrupar_conjuntos(lista_personajes,obtener_set(lista_personajes,"inteligencia"),"inteligencia")
                
                
        confirmacion = input("Desea realizar otra operacion")
        while confirmacion != "s" or confirmacion != "n":
            confirmacion = input("Desea realizar otra operacion?")
             
                    