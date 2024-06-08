from funciones_desafio_01 import *
from funciones_calculos import *
from funciones_conjuntos import *
from funciones_informes import *
from lib_filtrados import *
from funciones_calculos import *
def main():
    
    stark_normalizar_datos(lista_personajes)
    confirmacion = "s"
    bandera = False
    lista_femeninas = []
    lista_masculinos =[]
    bandera_mas_altos = False
    bandera_mas_bajos = False
    bandera_mas_altas = False
    bandera_mas_bajas = False
    
    
    mas_altos = []
    mas_altas=[]
    mas_bajos =[]
    mas_bajas = []
    
    
    #agregado
    
    
    while confirmacion == "s":
        menu()
        
        opcion = input ("ingrese opcion")
        while not validar_entero(opcion) or (validar_opcion(opcion)):
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
                bandera_mas_altos = True
                
                #listar_heroes(lista_fem_mas_altas)
                
            case "4":
                calcular_maximo_dos(lista_femeninas,"altura",mas_altas)
                listar_heroes(mas_altas)
                bandera_mas_altas = True
                

                
            case "5":
                calcular_minimo(lista_masculinos,"altura",mas_bajos)
                listar_heroes(mas_bajos)
                bandera_mas_bajos = True
                
            case "6":
                calcular_minimo(lista_femeninas,"altura",mas_bajas)
                listar_heroes(mas_bajas)
                bandera_mas_bajas = True
                    
            case "7":
                   
                promedio_altura_m = calcular_promedio_dos(lista_masculinos,"altura")
                mostrar_encabezado(f"La altura promedio de los superheroes masculinos es: {round(promedio_altura_m)}")
                    
            case "8":
                 promedio_altura_f = calcular_promedio_dos(lista_femeninas,"altura")
                 mostrar_encabezado(f"La altura promedio de los superheroes femeninos es: {round(promedio_altura_f)}")
                
            case "9":
                if bandera_mas_altos and bandera_mas_altas and bandera_mas_bajos and bandera_mas_bajas:
                    listar_por_criterio(mas_altos,"nombre")
                    listar_por_criterio(mas_altas,"nombre")
                    listar_por_criterio(mas_bajos,"nombre")
                    listar_por_criterio(mas_bajas,"nombre")
                else:
                    mostrar_encabezado("no se pueden mostrar los resultados sin haber realizado las operaciones anteriores")
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
        while confirmacion != "s" and confirmacion != "n":
            confirmacion = input("Desea realizar otra operacion?")
             
                    